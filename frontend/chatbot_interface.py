import streamlit as st
import requests
import os

st.title("📄 Applab Chatbot")

API_URL = os.getenv("API_URL", "http://backend:5000")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    pdf_path = os.path.join("uploads", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    files = {"file": open(pdf_path, "rb")}
    response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        st.success("PDF uploaded and processed successfully!")
    else:
        st.error("Error processing file.")

# Chat Interface
query = st.text_input("Ask a question")
if st.button("Ask") and query:
    try:
        response = requests.post(f"{API_URL}/chat", json={"query": query})

        if response.status_code == 200:
            data = response.json()

            st.write("### 🔍 Retrieved Chunks:")
            for i, chunk in enumerate(data.get("chunks", []), 1):
                st.write(f"**Chunk {i}:** {chunk}")

            st.write("### 💬 Answer:", data.get("response", "No response"))

        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with API: {e}")
