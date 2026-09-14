# Use an official Python runtime as a parent image
FROM python:3.12-slim

#change the working directory to /app
WORKDIR /app

# Upgrade underlying Debian OS packages to patch system CVEs
RUN apt-get update && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt    
COPY requirements.txt .

# Upgrade pip itself before installing requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app    
COPY . .

#expose the port that the Flask app will run on
EXPOSE 5000

#start the Flask app when the container starts
CMD ["python", "main.py"]