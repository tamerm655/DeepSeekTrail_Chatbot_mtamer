🚀 **Chatbot with RAG & Ollama**

This repository contains a Flask-based chatbot with Retrieval-Augmented Generation (RAG) powered by ChromaDB and Ollama for local LLM inference. It includes a Streamlit UI for interaction and is fully containerized using Docker & Docker Compose.

✨ **Features**

Document Upload & Processing: Extracts text from PDFs and stores chunked embeddings in ChromaDB.
Hybrid Retrieval: Uses semantic search + keyword filtering for improved response accuracy.
Ollama Integration: Runs DeepSeek-R1 1.5B locally for cost-effective inference.
Self-Verification: LLM checks its own responses for accuracy.
Direct Answer Mode: Returns exact matches without LLM generation when possible.
Streamlit Frontend: Simple, interactive UI for querying documents.
Dockerized Deployment: Run the entire system with docker-compose up.

🛠 **Tech Stack**

Backend: Flask, LangChain, ChromaDB, Ollama
Frontend: Streamlit
Infrastructure: Docker, Docker Compose

🚀 **Getting Started**

1️⃣ Clone the repo  
2️⃣ Run `docker-compose up --build`  
3️⃣ Open [http://localhost:8501](http://localhost:8501) in your browser  
4️⃣ Upload a PDF & start chatting!  