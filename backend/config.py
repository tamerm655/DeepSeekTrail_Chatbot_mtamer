import chromadb
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Configuration constants
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "deepseek-r1:1.5b" 

# Initialize embeddings and LLM
embedding_model = SentenceTransformer(EMBEDDING_MODEL)
llm = ChatOllama(model=LLM_MODEL, temperature=0)

# ChromaDB Setup
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="chatbot")

retriever = Chroma(
    persist_directory="chromadb_storage",
    embedding_function=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
).as_retriever()
