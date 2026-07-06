# Dockerfile for FraudLens Streamlit app

# Use the official lightweight Python image
FROM python:3.14-slim

# Install OS‑level dependencies (needed for pandas, numpy, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set a working directory
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt ./

# Install Python dependencies (including GPU‑aware packages if a GPU is present)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit (bind to all interfaces)
CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
