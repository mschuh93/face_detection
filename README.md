# Face Recognition Tool

## Beschreibung von Version 1 (Readme.md erstellt am 22.12.2024)

Dieses Tool verwendet die `face_recognition`-Bibliothek, um Gesichter in Bildern zu erkennen. Es identifiziert die Position von Gesichtern im Bild und markiert sie mit roten Rechtecken. Zusätzlich bietet es eine einfache Kommandozeilenoberfläche zur Nutzung.

## Features

- **Gesichtserkennung:** Erkennt alle Gesichter in einem Bild.
- **Visualisierung:** Zeichnet Rechtecke um die erkannten Gesichter.
- **Kommandozeilen-Schnittstelle:**  Nutzung über die Shell.

---

## Voraussetzungen

1. Python 3.7 oder höher
2. Installierte Python-Bibliotheken:
   - `click 8.1.7`
   - `dlib 19.24.6`
   - `face-recognition 1.3.0`
   - `face_recognition_models 0.3.0`
   - `numpy 2.1.2`
   - `pillow 11.0.0`
   - `pip 24.2`

### Installation der Abhängigkeiten

```bash
pip install face_recognition Pillow
```

---

## Nutzung

### Skript ausführen

Das Tool kann direkt über die Kommandozeile ausgeführt werden.

### Beispiel

1. Navigiere zum Verzeichnis des Projekts:

   ```bash
   cd <projektpfad>
   ```

2. Führe das Skript mit dem Bildpfad aus:

   ```bash
   python face_detection.py <image_path>
   ```

   Ersetze `<image_path>` mit dem Pfad zum Bild, das analysiert werden soll. Beispiel:

   ```bash
   python face_detection.py beispielbild.jpg
   ```

### Ergebnis

Das Skript:

- Zeigt die Anzahl der gefundenen Gesichter in der Konsole an.
- Öffnet das Bild mit roten Rechtecken um die erkannten Gesichter.

---

## Nächste Schritte

- **Fehlerbehandlung:** Robustere Handhabung ungültiger Eingaben.
- **Erweiterung:** Hinzufügen von Landmark-Erkennung (Augen, Mund, etc.).
- **Speicheroption:** Bearbeitetes Bild automatisch speichern.

---

## Beiträge

Pull Requests und Issues sind willkommen! Für Verbesserungsvorschläge oder Fehlerberichte erstelle bitte ein Issue im Repository.

