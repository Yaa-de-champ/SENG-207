#FROM ubuntu:latest
#LABEL authors="Lenovo"
#
#ENTRYPOINT ["top", "-b"]

# Use an official lightweight Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for text-to-speech and GUI support
RUN apt-get update && apt-get install -y \
    libasound2 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Copy all files from your project directory to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the app
CMD ["python", "SENG207_Project2_Task1.py"]
