from flask import Flask, request, jsonify
import os
from app.processing import store_chunks
from app.retrieval import search
from app.llm import generate_response

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

latest_uploaded_filename = None  # Global variable to track last uploaded file

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/upload", methods=["POST"])
def upload():
    """Handles PDF uploads and processes them."""
    global latest_uploaded_filename

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    latest_uploaded_filename = file.filename  # Update last uploaded filename
    store_chunks(pdf_path, latest_uploaded_filename)  # Pass filename for metadata tracking

    return jsonify({"message": "File processed successfully"})

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot queries."""
    try:
        global latest_uploaded_filename
        if not latest_uploaded_filename:
            return jsonify({"error": "No document uploaded yet."}), 400

        data = request.json
        if not data or "query" not in data:
            return jsonify({"error": "Missing query parameter"}), 400

        query = data["query"]
        retrieved_chunks = search(query, latest_uploaded_filename)

        if not retrieved_chunks:
            return jsonify({"response": "No relevant information found.", "chunks": []})

        response = generate_response(query, retrieved_chunks)

        # Extract response text properly
        response_text = response.content if hasattr(response, "content") else str(response)

        return jsonify({"response": response_text, "chunks": retrieved_chunks})

    except Exception as e:
        print("⚠️ API Error:", str(e))  # Debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
