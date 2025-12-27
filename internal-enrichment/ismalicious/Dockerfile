FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/opencti-connector-ismalicious

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

ENTRYPOINT ["python", "-m", "src"]
