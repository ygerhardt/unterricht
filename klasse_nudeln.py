# klasse_pizza.py

import pygame
import sys
from klasse_italienisches_essen import Italienisches_Essen

class Nudeln(Italienisches_Essen):
    """
    Klasse, die ein Nudelgericht darstellt.
    """

    def __init__(self, anzahl, pasta_typ=Italienisches_Essen.default_pasta, sauce_typ=Italienisches_Essen.default_sauce, scharf=Italienisches_Essen.scharf, extrakaese=Italienisches_Essen.extrakaese):
        """
        Konstruktor der Klasse Nudeln.

        Args:
            anzahl (int): Anzahl der Nudelportionen.
            scharf (bool): Wahr, wenn das Gericht scharf sein soll.
            extrakaese (bool): Wahr, wenn zusätzlicher Käse gewünscht ist.
            pasta_typ (str): Typ der Pasta.
            sauce_typ (str): Typ der Sauce.
        """
        super().__init__(anzahl, scharf, extrakaese)
        self.pasta_typ = pasta_typ
        self.sauce_typ = sauce_typ

    def nudeln_herstellen(self):
        """
        Zeigt ein Bild des Nudelgerichts mithilfe von Pygame.
        Erfordert Pygame und einen gültigen Bildpfad.
        """
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

    def essen_kochen(self):
        """
        Bereitet die Nudeln zu und speichert die Beschreibung der Zubereitung.
        """
        extras = []
        if self.scharf:
            extras.append("Zusätzlich scharf gewürzt")
        if self.extrakaese:
            extras.append("mit extra Käse")

        extras_str = " und ".join(extras)
        self.zubereitungsdetails = (f"{self.anzahl}x Nudeln der Sorte {self.pasta_typ} werden mit {self.sauce_typ} zubereitet. "
                                    f"{extras_str}")

    def __str__(self):
        """
        Gibt die finale Beschreibung des Nudelgerichts zurück, inklusive der Zubereitungsdetails.
        """
        return self.zubereitungsdetails


