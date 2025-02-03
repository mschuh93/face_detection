# Schlankes Basis-Image nutzen
FROM python:3.9-alpine

# Arbeitsverzeichnis setzen
WORKDIR /app

# Notwendige Systempakete für dlib und face_recognition
RUN apk add --no-cache \
    build-base \
    cmake \
    openblas-dev \
    lapack-dev \
    libx11-dev \
    libffi-dev \
    libpng-dev \
    tiff-dev \
    jpeg-dev \
    git

# Abhängigkeiten installieren
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Flask-App-Code kopieren
COPY . .

# Flask-App starten
CMD ["python3", "app.py"]
