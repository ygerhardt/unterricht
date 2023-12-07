# klasse_italienisches_essen.py

class Italienisches_Essen:
    """
    Oberklasse für italienische Gerichte.

    Attribute:
        anzahl (int): Anzahl der Portionen.
        list_sauce (list): Liste verfügbarer Saucen.
        list_zutat (list): Liste verfügbarer Zutaten
        list_pasta (list): Liste verfügbarer Pastasorten
        default_sauce (str): Standardsauce für das Gericht.
        default_zutat (str): Standardzutat für das Gericht.
        default_pasta (str): Standardpastasorte für das Gericht.
        scharf (bool): Gibt an, ob das Gericht scharf sein soll.
        extrakaese (bool): Gibt an, ob zusätzlicher Käse hinzugefügt werden soll.
    """
    anzahl = 0
    list_sauce = ["Tomatensauce", "Hollandaisesauce", "Carbonarasauce", "Barbecue", "Creme Fraiche"]
    list_zutat = ["Salami", "Pilze", "Hackfleisch", "Schinken", "Paprika", "Oliven"]
    list_pasta = ["Spaghetti", "Rigatoni", "Penne"]
    default_sauce = list_sauce[0]
    default_zutat = list_zutat[0]
    default_pasta = list_pasta[0]
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
