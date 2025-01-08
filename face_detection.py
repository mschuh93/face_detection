import argparse
import face_recognition
import os

from PIL import Image, ImageDraw
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__) # Erstellt die Flask-Anwendung. App bekommt den Namen main, wenn es aus der Konsole gestartet wird. 

@app.route('/') # Definiert die Route für die Startseite. Wird einfach nur http://127.0.0.1:5000 aufgerufen kommt man auf die Startseite
def index(): 
    return render_template('index.html') # Lädt die HTML-Datei für die Startseite 



if __name__ == '__main__': # App wird nur ausgeführt, wenn sie direkt aus dem Terminal gestartet wird -> dann __name__ = __main__ sonst __name__ = Dateiname ohne .py
    app.run(debug=True) # Startet den Flask-Server mit app.run() auf http://127.0.0.1:5000 debug=True fügt zusätzlich einen Debug-Modus hinzu der einen informiert, wenn im code etwas schiefgeht. 

@app.route('/uploads', methods=['POST']) #Route für eine POST-Anfrage um Bilder hochzuladen
def upload_file():
    if 'file' not in request.files: # Überprüfen, ob eine Datei hochgeladen wurde wenn nicht dann ->
        return "Keine Datei hochgeladen! Bitte prüfen.", 400
    
    file = request.files['file'] # Holt die hochgeladene Datei welche in request.file ist und ordnet sie der Variable file zu.
    if file.filename == '': # Prüft, ob der Dateiname leer ist
        return "Datei hat keinen Namen. Bitte vergeben.", 400

    #Datei speichern 
    file_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True) # Erstellt ein Verzeichnis, falls es noch nicht exisiterit 
    file.save(file_path) # speichert die Datei lokal

    # Gesichtserkennung durchführen 
    result_path = detect_faces(file_path)

    # Weiterleitung zur Ergebnisseite 
    return redirect(url_for('show_result', image=result_path)) 




def detect_faces(image_path):
    # Bild laden
    image = face_recognition.load_image_file(image_path)

    # Gesichter im Bild finden
    face_locations = face_recognition.face_locations(image)

    print(f"Es wurden {len(face_locations)} Gesichter im Bild gefunden.")

    # Bild mit den erkannten Gesichtern öffnen und bearbeiten
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    # Rechtecke um die erkannten Gesichter zeichnen
    for (top, right, bottom, left) in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline="red", width=3)

    #Ergebnis speichern 
    result_path = os.path.join('uploads','result_' + os.path.basename(image_path))
    # os.path.join('uploads',...) : Diese Funktion kombiniert den Ordner uploads mit einem Dateinamen zu einem vollständigen Pfad.
    # Dadurch wird sichergestellt, dass der Pfad betriebssystemunabhängig korrekt ist (z. B. / auf macOS/Linux, \\ auf Windows).
    # 'result_' + os.path.basename(image_path):

    # os.path.basename(image_path) gibt den Dateinamen aus einem vollständigen Pfad zurück, z. B.:
    # Eingabe: /path/to/image.jpg
    # Ausgabe: image.jpg
    # 'result_' wird vor den Dateinamen gesetzt, sodass der neue Name z. B. result_image.jpg lautet.
    # Ergebnis:
    # result_path enthält den vollständigen Pfad, unter dem das Ergebnisbild gespeichert wird:
    # Beispiel: uploads/result_image.jpg
    #     pil_image.save(result_path)

    return 'result_' + os.path.basename(image_path)

# Route für das Ergebnis anzeigen 
@app.route ('/results')
def show_results():
    image = request.args.get('image') #holt den Bildpfad aus der Anfrage 
    return render_template('result.html', image=image) 

# Erstellt die Route, um hochgeladene Dateien bereitzustellen 
@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory('uploads', filename) #send_from_directory: Flask stellt Dateien aus einem Ordner bereit.


def main(): 
    #Argument Parser erstellen 
    parser = argparse.ArgumentParser(description="Gesichtserkennung im Bild")
    
    #Bildpfad als Argument hinzufügen 
    parser.add_argument("image_path", type=str, help="Der Pfad zum Bild")
    
    #Argument parsen aus der Shell
    args = parser.parse_args()

    # Gesichtserkennung ausführen
    detect_faces(args.image_path)

# Hauptprogramm
if __name__ == "__main__":
    main()
