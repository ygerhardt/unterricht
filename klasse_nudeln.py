# klasse_pizza.py

import pygame
import sys
from klasse_italienisches_essen import Italienisches_Essen

class Nudeln(Italienisches_Essen):
    """
    Klasse, die ein Nudelgericht darstellt.

    Attribute:
        pasta_typ (str): Typ der Pasta für das Gericht.
        sauce_typ (str): Typ der Sauce für das Gericht.
    """

    def __init__(self, anzahl, pasta_typ=Italienisches_Essen.default_pasta, sauce_typ=Italienisches_Essen.default_sauce, scharf=Italienisches_Essen.scharf, extrakaese=Italienisches_Essen.extrakaese):
        """
        Konstruktor der Klasse Nudeln.

        Args:
            anzahl (int): Anzahl der Nudelportionen.
            pasta_typ (str): Typ der Pasta.
            sauce_typ (str): Typ der Sauce.
            scharf (bool): Wahr, wenn das Gericht scharf sein soll.
            extrakaese (bool): Wahr, wenn zusätzlicher Käse gewünscht ist.
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
        Gibt eine Beschreibung des Nudelgerichts mit Details zu Pasta-Typ, Sauce und weiteren Eigenschaften zurück.

        Returns:
            str: Beschreibung des Nudelgerichts.
        """
        zubereitung = f"Nudeln der Sorte {self.pasta_typ} werden mit {self.sauce_typ} zubereitet."
        if self.scharf:
            zubereitung += " Zusätzlich scharf gewürzt."
        if self.extrakaese:
            zubereitung += " Mit extra Käse serviert."
        return zubereitung

    def __str__(self):
        """
        Gibt eine Beschreibung des Nudelgerichts zurück.

        Returns:
            str: Beschreibung des Nudelgerichts.
        """
        return f"Nudelgericht {self.pasta_typ} mit {self.sauce_typ}. Sauce: {self.default_sauce}. Scharf: {self.scharf}, Extrakäse: {self.extrakaese}"


