# Use the Python 3.11-slim base image
FROM python:3.11-slim

# Set the working directory to the specified folder
WORKDIR /app

# Copy the service files to the working directory
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary ports
EXPOSE 8000

# Define the command to run the service
CMD ["python", "app.py"]