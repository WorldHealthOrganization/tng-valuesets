# Start from the official Python image
FROM python:3.13.0a4-slim

# Set the working directory in the container
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Copy the Python script and requirements file into the working directory
COPY valueset-importer.py requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python script
CMD ["python", "./valueset-importer.py"]