# Basis-Image mit Python 3.9
FROM python:3.9-slim

# Abreitsverzeichnis im Container
WORKDIR /app

# Abhänigkeiten kopieren und installieren
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flask-App-Code kopieren
COPY . . 

# Flask-App starten 
CMD ["python", "app.py"]