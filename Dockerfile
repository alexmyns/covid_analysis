# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /covid_analysis

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app file to the container
COPY . .

# Set the command to run when the container starts
CMD ["streamlit", "run", "--server.port", "8501", "Home.py"]
