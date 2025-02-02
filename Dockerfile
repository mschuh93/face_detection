# Basis-Image mit Python 3.9
FROM python:3.9-slim

# Systempakete für face_recognition installieren
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libglib2.0-0


# Arbeitsverzeichnis im Container
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy && \
    pip install --no-cache-dir -r requirements.txt

# Flask-App-Code kopieren
COPY . .

# Flask-App starten
CMD ["python", "app.py"]
