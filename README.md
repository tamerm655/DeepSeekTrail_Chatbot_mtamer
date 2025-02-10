# Applab Cahtbot

This repository contains a chatbot that retrieves and generates responses using ChromaDB for vector search. The system is designed to work with structured document retrieval, ensuring that responses are accurate and context-aware.

## Features

- **Flask API**: Handles requests, processes user input, and retrieves relevant information.
- **Streamlit Interface**: A simple web-based UI for interacting with the chatbot.
- **ChromaDB for Vector Search**: Stores document embeddings and retrieves relevant chunks based on similarity.
- **Hybrid Search**: Combines ChromaDB’s vector search with keyword-based filtering.
- **Overlapping Sliding Window & Semantic Chunking**: Improves retrieval accuracy by splitting documents into meaningful sections.
- **Re-ranking**: Uses free tools like `text-embedding-ada-002` to improve search results.
- **Direct Answer Mode**: If an exact match is found, the chatbot returns the text without involving the LLM.
- **Self-Verification**: The LLM cross-checks its own answers to improve reliability.
- **Debugging View**: Displays retrieved text chunks for transparency.
- **LangChain’s RetrievalQA**: Manages document retrieval and response generation.

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies (for backend and frontend)**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask API**
   ```bash
   python api.py
   ```

5. **Run the Streamlit Interface**
   ```bash
   streamlit run app.py
   ```

## Configuration

- **Documents**: Place PDF files in the `data/` folder. The system will process and store embeddings automatically.
- **Environment Variables**: Store API keys and configuration details in a `.env` file.

## Deployment with Docker

1. **Build the Docker Image**
   ```bash
   docker build -t rag-chatbot .
   ```
2. **Run the Container**
   ```bash
   docker run -p 5000:5000 rag-chatbot
   ```