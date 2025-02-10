# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose ports for Flask and Streamlit
# EXPOSE 5000

# Start both Flask and Streamlit apps
CMD ["streamlit", "run", "chatbot_interface.py"]