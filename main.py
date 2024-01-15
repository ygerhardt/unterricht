import json
import os
import tkinter as Tk
import pygame
import sys
from klasse_pizza import Pizza
from klasse_pasta import Pasta
from PIL import Image, ImageTk

# dateioperationen
def lade_datenbank():
    try:
        with open("data/datenbank.json", "r") as file:
             return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Fehler beim Laden der Datenbank: {e}")
        sys.exit("Das Programm wird beendet, da die Datenbank nicht geladen werden kann.")
        
def speichere_bestellung(bestellung, gesamtpreis):
    bestellungen = []
    bestellungen.append({"Bestellung": bestellung, "Gesamtpreis": gesamtpreis})

    try:
        with open("data/bestellung.json", "w") as file:
            json.dump(bestellungen, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Fehler beim Schreiben der Bestellungsdatei: {e}")
        sys.exit("Das Programm wird beendet.")

# bild und sound
def zeige_bild():
    root = Tk.Tk()
    root.title("Bildanzeige für das gewählte Gericht")
    root.attributes("-topmost", True)

    img = Image.open("data/bilder/nudeln_spaghetti.jpg")
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

def verarbeite_bestellung(gericht, datenbank):
    zeige_bild()
    bestellung = gericht(datenbank)
    auswahl = bestellung.waehle_groesse() if isinstance(bestellung, Pizza) else bestellung.waehle_sorte()
    bestell_details = bestellung.erfasse_bestellung(auswahl)
    preis = zeige_bestellung_und_preis(bestellung)
    speichere_bestellung(bestell_details, preis)
    return preis

def main():
    datenbank = lade_datenbank()
    gesamtpreis = 0

    while True:
        auswahl = input("Willkommen im Restaurant 'FIAE A'. Was möchten Sie bestellen? (01: Pizza, 02: Pasta): ")
        print()
        if auswahl == "01":
            gesamtpreis += verarbeite_bestellung(Pizza, datenbank)
        elif auswahl == "02":
            gesamtpreis += verarbeite_bestellung(Pasta, datenbank)
        else:
            print("Ungültige Auswahl. Bitte wählen Sie '01' für Pizza oder '02' für Pasta.\n")
            continue

        fortsetzen = input("\nDarf es noch etwas sein? (ja/nein): ").lower()
        if fortsetzen == 'ja':
            print()
            continue
        else:
            spiele_sound()
            break

    print(f"\nVielen Dank für Ihre Bestellung! Bitte bezahlen Sie {gesamtpreis:.2f}\u20AC.")

    if os.path.exists("data/bestellung.json"):
        os.remove("data/bestellung.json")

if __name__ == "__main__":
    main()


