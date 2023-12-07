# klasse_pizza.py

from klasse_italienisches_essen import Italienisches_Essen

class Pizza(Italienisches_Essen):
    """
    Klasse, die eine Pizza darstellt.

    Attribute:
        pizzaAnzahl (int): Gesamtanzahl der bisher erstellten Pizzas.
        gueltigeZutaten (list): Liste gültiger Zutaten für die Pizza.
        gueltigeSaucen (list): Liste gültiger Saucen für die Pizza.
    """

    def __init__(self, anzahl, zutat_1=Italienisches_Essen.default_zutat, zutat_2=Italienisches_Essen.default_zutat, zutat_3=Italienisches_Essen.default_zutat, sauce=Italienisches_Essen.default_sauce, scharf=Italienisches_Essen.scharf, extrakaese=Italienisches_Essen.extrakaese):
        """
        Konstruktor der Klasse Pizza.

        Args:
            anzahl (int): Anzahl der Pizzas.
            zutat_1, zutat_2, zutat_3 (str): Zutaten für die Pizza.
            scharf (bool): Wahr, wenn die Pizza scharf sein soll.
            extrakaese (bool): Wahr, wenn zusätzlicher Käse gewünscht ist.
        """
        super().__init__(anzahl, scharf, extrakaese)
        self.zutat_1 = zutat_1
        self.zutat_2 = zutat_2
        self.zutat_3 = zutat_3
        self.default_sauce = sauce

    def pizza_belegen(self, z_1, z_2, z_3):
        """
        Ändert die Zutaten der Pizza.

        Args:
            z_1, z_2, z_3 (str): Die neuen Zutaten für die Pizza.
        """
        self.zutat_1 = z_1
        self.zutat_2 = z_2
        self.zutat_3 = z_3

    def essen_kochen(self):
        """
        Bereitet die Pizza zu und gibt eine Beschreibung des Vorgangs zurück.

        Returns:
            str: Beschreibung der Zubereitung der Pizza, einschließlich der verwendeten Zutaten und ob sie scharf oder mit extra Käse zubereitet wird.
        """
        zubereitung = f"Pizza wird mit {self.zutat_1}, {self.zutat_2}, {self.zutat_3} belegt."
        zubereitung += f" Gebacken mit {self.default_sauce}sauce."
        if self.scharf:
            zubereitung += " Zusätzlich scharf gewürzt."
        if self.extrakaese:
            zubereitung += " Extra Käse hinzugefügt."
        return zubereitung

    def __str__(self):
        """
        Gibt eine Beschreibung der Pizza zurück.

        Returns:
            str: Beschreibung der Pizza, einschließlich Zutaten, Standardsoße und Gesamtanzahl der Pizzas. 
        """
        return f"Pizza mit {self.zutat_1}, {self.zutat_2}, {self.zutat_3}. Sauce: {self.default_sauce}. Scharf: {self.scharf}, Extrakäse: {self.extrakaese}"

