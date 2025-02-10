# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | bash

# Ensure Ollama is available in PATH
ENV PATH="/root/.ollama/bin:$PATH"

# Start Ollama in the background and wait for it to be ready
RUN ollama serve & \
    sleep 10 && \
    ollama pull deepseek-r1:1.5b

# Copy the rest of the application code to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Download NLTK data (punkt and punkt_tab)
RUN python -m nltk.downloader punkt punkt_tab

# Expose ports for Flask and Streamlit
EXPOSE 5000

# Start Ollama in the background and then run the Flask app
CMD ollama serve & python main.py