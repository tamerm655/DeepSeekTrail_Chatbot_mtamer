import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize
from config import embedding_model, collection


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text("text") for page in doc])


def process_text(text, chunk_size=4, overlap=1):
    """Processes text into overlapping chunks."""
    text = re.sub(r'[^a-zA-Z0-9 .?@/: \n]', '', text)
    text = re.sub(r' +', ' ', text)
    sentences = sent_tokenize(text)
    return [" ".join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size - overlap)]


def get_embedding(text):
    """Generates an embedding for the given text."""
    return embedding_model.encode(text).tolist()


def store_chunks(pdf_path, filename):
    """Extracts, processes, and stores text chunks in ChromaDB with filename metadata."""

    # Delete old chunks from the same document
    collection.delete(where={"filename": filename})

    text = extract_text_from_pdf(pdf_path)
    chunks = process_text(text)

    if not chunks:
        print(f"⚠️ No text found in {filename}")
        return []

    # Generate embeddings in batch for efficiency
    embeddings = [get_embedding(chunk) for chunk in chunks]

    # Prepare data for ChromaDB
    ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"filename": filename} for _ in chunks]

    # Store chunks in ChromaDB
    collection.add(ids=ids, documents=chunks, embeddings=embeddings, metadatas=metadatas)

    print(f"✅ {len(chunks)} chunks from '{filename}' stored in ChromaDB")
    return chunks
