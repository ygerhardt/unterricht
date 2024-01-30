import json
import os
import tkinter as Tk
import pygame
import sys
from classes.klasse_pizza import Pizza
from classes.klasse_pasta import Pasta
from classes.klasse_eis import Eis
from classes.klasse_getraenke import Getraenke
from PIL import Image, ImageTk

# setze absoluten Pfad
def setze_root_verzeichnis():
    """
    Setzt das Verzeichnis, in dem das ausführende Skript liegt, als Root-Verzeichnis.
    """
    abspath = os.path.abspath(__file__)  # Absoluter Pfad der ausführenden Datei
    dname = os.path.dirname(abspath)  # Verzeichnisname der Datei
    os.chdir(dname)  # Wechsle das aktuelle Arbeitsverzeichnis zu diesem Verzeichnis

# dateioperationen
def lade_datenbank():
    try:
        with open("data/datenbank.json", "r") as file:
             return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"\nFehler beim Laden der Datenbank: {e}")
        sys.exit("Das Programm wird beendet, da die Datenbank nicht geladen werden kann.\n")
        
def speichere_bestellung(bestellung, gesamtpreis):
    bestellungen = []
    bestellungen.append({"Bestellung": bestellung, "Gesamtpreis": gesamtpreis})

    try:
        with open("data/bestellung.json", "w") as file:
            json.dump(bestellungen, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"\nFehler beim Schreiben der Bestellungsdatei: {e}")
        sys.exit("Das Programm wird beendet.\n")

# bild und sound
def zeige_bild(bildpfad):
    root = Tk.Tk()
    root.title("Bildanzeige für das gewählte Gericht")
    root.attributes("-topmost", True)

    img = Image.open(bildpfad)
    tk_img = ImageTk.PhotoImage(img)
    label = Tk.Label(root, image=tk_img)
    label.pack()

    continue_button = Tk.Button(root, text="Weiter", command=root.destroy)
    continue_button.pack()

    root.mainloop()

def spiele_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("data/sounds/sound_microwave_ding.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.delay(100)

# preisberechnung und verarbeitung
def zeige_bestellung_und_preis(gericht):
    print("\nIhre Bestellung:", gericht.zubereitungsdetails)
    preis = sum(gericht.zutaten.values())
    print(f"Preis: {preis:.2f}\u20AC") # \u20AC = €
    return preis

def verarbeite_bestellung(gericht, datenbank, bildpfad):
    bestellung = gericht(datenbank)
    bestell_details = bestellung.erfasse_bestellung()
    preis = zeige_bestellung_und_preis(bestellung)
    speichere_bestellung(bestell_details, preis)
    zeige_bild(bildpfad)
    return preis

# main
def main():
    setze_root_verzeichnis()
    datenbank = lade_datenbank()
    gesamtpreis = 0
    
    while True:
        auswahl = input("Willkommen im Restaurant 'FIAE A'. Was möchten Sie tun? (01: Pizza bestellen, 02: Pasta bestellen, 03: Eis bestellen, 04: Getraenke bestellen, 05: Beenden): ")
        print()
        if auswahl == "01":
            gesamtpreis += verarbeite_bestellung(Pizza, datenbank, "data/bilder/pizzastock.jpg")
        elif auswahl == "02":
            gesamtpreis += verarbeite_bestellung(Pasta, datenbank, "data/bilder/nudeln_spaghetti.jpg")
        elif auswahl == "03":
            gesamtpreis += verarbeite_bestellung(Eis, datenbank, "data/bilder/stockice.jpg")
        elif auswahl == "04":
            gesamtpreis += verarbeite_bestellung(Getraenke, datenbank, "data/bilder/getraenke.jpg")
        elif auswahl == "05": sys.exit("\nDas Programm wird beendet.\n")
        else:
            print("Ungültige Auswahl. Bitte wählen Sie '01' für Pizza, '02' für Pasta oder '03' für Eis.\n")
            continue

        fortsetzen = input("\nDarf es noch etwas sein? (ja/nein): ").lower()
        if fortsetzen != 'nein':
            print()
            continue
        else:
            spiele_sound()
            break

    print(f"\nVielen Dank für Ihre Bestellung! Bitte bezahlen Sie {gesamtpreis:.2f}\u20AC.")
    os.remove("data/bestellung.json")

if __name__ == "__main__":
    main()


