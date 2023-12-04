import pygame
import sys

# planmäßig als attribut von oben
# anzahl                #atm prov. lokal
# list_sauce = ("Hackfleischsauce", "Tomatensauce", "Carbonarasauce")   #atm prov. lokal
# scharf                #atm prov. lokal
# extrakäse             #atm prov. lokal
# scharf                #atm prov. lokal
# extrakaese            #atm prov. lokal
list_pasta = ("Spagetti", "Rigatoni", "Penne")
list_sauce = ("Tomatensauce", "Hackfleischsauce", "Carbonarasauce")


class Nudeln():
    """
        Klasse, die ein Nudelgericht darstellt.

        Attribute:
            pas (int): Auswahl der Pasta über Element aus Liste
            sau (int): Auswahl der Sauce über Element aus Liste
            scha (bool): Scharf ja/nein
            exkae (bool): Extrakäse ja/nein


        Methoden:
            __init__: Konstruktor, der ein neues Nudelgericht erstellt
            nudeln_herstellen: gibt ein Bild bei Ausruf aus
            __str__(): Gibt eine Beschreibung des Nudelgerichtes zurück.
    """

    def __init__(self, pas, sau, scha, exkae):
        self.pasta = list_pasta[pas]
        self.sauce = list_sauce[sau]
        self.scharf = scha
        self.extrakaese = exkae


    def nudeln_herstellen(self):
        pygame.init()
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        image_path = r'nudeln_spaghetti.jpg'  #C:\Users\Umschueler\...
        pygame.display.set_caption(f'{image_path}')
        image = pygame.image.load(image_path)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(image, (0, 0))
            pygame.display.flip()

    def __str__(self):
        """
        Gibt eine Beschreibung des Nudelgerichts zurück.

        Returns:
            str: Beschreibung des Nudelgerichts.
        """
        return f"Nudelgericht {self.pasta} mit {self.sauce}\nScharf:{self.scharf} Extrakäse:{self.extrakaese}"


