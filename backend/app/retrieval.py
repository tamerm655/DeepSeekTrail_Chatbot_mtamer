from config import collection
from app.processing import get_embedding

def search(query, filename, top_k=5):
    """Retrieves relevant chunks based on query, filtered by filename."""
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"filename": filename}  
    )

    retrieved_chunks = results["documents"] if results else []

    print(f"🔍 Query: {query}")
    print(f"📂 Retrieved Chunks from {filename}:", retrieved_chunks if retrieved_chunks else "No chunks found")

    return retrieved_chunks
