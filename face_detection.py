import argparse
import face_recognition

from PIL import Image, ImageDraw

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

    # Bild anzeigen
    pil_image.show()

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
