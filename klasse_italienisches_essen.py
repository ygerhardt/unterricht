# klasse_italienisches_essen.py

class Italienisches_Essen:
    """
    Oberklasse für italienische Gerichte.

    Attribute:
        anzahl (int): Anzahl der Portionen.
        list_sauce (list): Liste verfügbarer Saucen.
        default_sauce (str): Standard-Sauce für das Gericht.
        scharf (bool): Gibt an, ob das Gericht scharf sein soll.
        extrakaese (bool): Gibt an, ob zusätzlicher Käse hinzugefügt werden soll.
    """
    anzahl = 0
    list_sauce = ["Tomatensauce", "Hollandaisesauce", "Carbonarasauce"]
    default_sauce = list_sauce[0]
    scharf = False
    extrakaese = False

    def __init__(self, anzahl, scharf, extrakaese):
        """
        Konstruktor der Klasse Italienisches_Essen.

        Args:
            anzahl (int): Anzahl der Portionen.
            scharf (bool): Wahr, wenn das Gericht scharf sein soll.
            extrakaese (bool): Wahr, wenn zusätzlicher Käse gewünscht ist.
        """
        self.anzahl = anzahl
        self.scharf = scharf
        self.extrakaese = extrakaese


def essen_kochen():
    """
        Methode zum Kochen des Essens.
        Soll in Unterklassen überschrieben werden.
    """
    pass
