import json
import os
import tkinter as Tk
import pygame
import sys
from classes.backend.klasse_speisen import Speisen
from classes.backend.klasse_dessert import Dessert
from classes.backend.klasse_getraenke import Getraenke
from PIL import Image, ImageTk

# setze absoluten Pfad
def setze_root_verzeichnis():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath) 
    os.chdir(dname) 

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
    print("Ihre Bestellung:", gericht.zubereitungsdetails)
    preis = sum(gericht.zutaten.values())
    print(f"Preis: {preis:.2f}\u20AC") # \u20AC = €
    return preis

def verarbeite_bestellung(gericht, datenbank, bildpfad, gericht_typ=None):
    if gericht_typ is None:
        bestellung = gericht(datenbank)
    else:
        bestellung = gericht(datenbank, gericht_typ)
    bestell_details = bestellung.erfasse_bestellung()
    preis = zeige_bestellung_und_preis(bestellung)
    speichere_bestellung(bestell_details, preis)
    zeige_bild(bildpfad)
    return preis

def zeige_gesamte_bestellung():
    try:
        with open("data/bestellung.json", "r") as file:
            bestellungen = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"\nFehler beim Laden der Bestellungsdatei: {e}")
        sys.exit("Das Programm wird beendet.\n")

    print("\nIhre gesamte Bestellung:")
    for i, bestellung in enumerate(bestellungen, 1):
        print(f"\nBestellung {i}:")
        bestellungsdetails = ', '.join(f"{zutat}: {preis:.2f}\u20AC" for zutat, preis in bestellung["Bestellung"].items())
        print("Bestellungsdetails:", bestellungsdetails)
        print(f"Gesamtpreis: {bestellung['Gesamtpreis']:.2f}\u20AC")

# main
def main():
    setze_root_verzeichnis()
    datenbank = lade_datenbank()
    gesamtpreis = 0

    menu_optionen = {
        "01": {"klasse": Speisen, "bild": "data/bilder/pizzastock.jpg", "gericht_typ": "Pizza"},
        "02": {"klasse": Speisen, "bild": "data/bilder/nudeln_spaghetti.jpg", "gericht_typ": "Pasta"},
        "03": {"klasse": Dessert, "bild": "data/bilder/stockice.jpg"},
        "04": {"klasse": Getraenke, "bild": "data/bilder/getraenke.jpg"},
    }

    while True:
        auswahl = input("Willkommen im Restaurant 'FIAE A'. Was möchten Sie tun? (01: Pizza bestellen, 02: Pasta bestellen, 03: Eis bestellen, 04: Getraenke bestellen, 05: Beenden): ")
        print()
        if auswahl in menu_optionen:
            option = menu_optionen[auswahl]
            gesamtpreis += verarbeite_bestellung(option["klasse"], datenbank, option["bild"], gericht_typ=option.get("gericht_typ"))
        elif auswahl == "05": sys.exit("Das Programm wird beendet.\n")
        else:
            print("Ungültige Auswahl. Bitte wählen Sie '01' Pizza, '02' für Pasta ,'03' für Eis, '04' für Getraenke oder '05' für Beenden.\n")
            continue

        while True:
            fortsetzen = input("\nDarf es noch etwas sein? (ja/nein): ").lower()
            if fortsetzen == 'ja':
                print()
                break
            elif fortsetzen == 'nein':
                zeige_gesamte_bestellung()
                print(f"\nVielen Dank für Ihre Bestellung! Bitte bezahlen Sie {gesamtpreis:.2f}\u20AC.")
                os.remove("data/bestellung.json")
                return
            else:
                print("\nUngültige Eingabe. Bitte antworten Sie mit 'ja' oder 'nein'.")

if __name__ == "__main__":
    main()


