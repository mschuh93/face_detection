# Face Recognition App

## Beschreibung von Version 1 (Readme.md erstellt am 12.01.2025)

## Beschreibung
Dies ist eine Flask-basierte Webanwendung, die Bilder hochladen, verarbeiten und Gesichtserkennung durchführen kann. Momentan wird das hochgeladene Bild verarbeitet, und Ergebnisse wie erkannte Gesichter und bearbeitete Bilder werden angezeigt. Der Code ist aktuell in der Entwicklung und nicht vollständig funktional.

---

## **Funktionen**

### **Funktionalität des aktuellen Codes:**
1. **Hochladen von Bildern:**
   - Benutzer können ein Bild im `.jpg`- oder `.png`-Format hochladen.
   - Die hochgeladene Datei wird im Verzeichnis `uploads/` gespeichert.

2. **Gesichtserkennung:**
   - Der Code versucht, Gesichter im Bild zu erkennen und ein bearbeitetes Bild mit markierten Gesichtern zu speichern.
   - Das bearbeitete Bild wird im selben Verzeichnis gespeichert und kann aufgerufen werden.

3. **Ergebnisseite:**
   - Zeigt an, ob Gesichter erkannt wurden, und liefert das bearbeitete Bild oder eine Fehlermeldung zurück.

### **Einschränkungen und Probleme:**
- **404-Fehler:** Es gibt ein bekanntes Problem, bei dem nach dem Hochladen ein Fehler auftritt, weil eine falsche Route aufgerufen wird.
- **Keine erkannte Gesichter:** Aktuell werden Gesichter in den hochgeladenen Bildern nicht immer zuverlässig erkannt.
- **Debugging aktiv:** Der Code enthält Debugging-Logs, um aktuelle Fehler besser nachzuvollziehen.

---

## **Installationsanleitung**

1. **Voraussetzungen:**
   - Python 3.7 oder höher
   - Virtuelle Umgebung empfohlen

2. **Abhängigkeiten installieren:**
   ```bash
   pip install flask face_recognition Pillow
   ```

3. **Projektstruktur:**
   ```
   project/
   ├── app.py                # Hauptcode der Anwendung
   ├── templates/            # HTML-Vorlagen
   │   ├── index.html        # Startseite
   │   └── results.html      # Ergebnisseite
   ├── uploads/              # Verzeichnis für hochgeladene Dateien
   └── requirements.txt      # Abhängigkeiten
   ```

4. **App starten:**
   ```bash
   python app.py
   ```

5. **Zugriff auf die App:**
   - Öffne deinen Browser und navigiere zu: `http://127.0.0.1:5000`

---

## **Aktuelle Entwicklung**
- Der Code ist nicht final und befindet sich in der Debugging-Phase.
- Bekannte Probleme:
  1. **Falsche Weiterleitungen:** Nach dem Upload wird eine fehlerhafte Route (`/uploads`) aufgerufen.
  2. **Gesichtserkennung:** Gesichter werden nicht immer erkannt oder markiert.

### **Nächste Schritte:**
1. Debugging der Upload-Route und Ergebnisseite.
2. Verlässliche Gesichtserkennung mit kleineren Testbildern sicherstellen.
3. Erweiterung der App um detaillierte Fehlermeldungen und Benutzerführung.

---

## Beiträge
Pull Requests und Vorschläge sind willkommen. Dieses Projekt eignet sich gut, um mehr über Flask, Gesichtserkennung und Webentwicklung zu lernen.

