# klasse_pizza.py

from klasse_italienisches_essen import Italienisches_Essen

class Pizza(Italienisches_Essen):
    """
    Klasse, die eine Pizza darstellt.
    """

    def __init__(self, anzahl, zutat_1=Italienisches_Essen.default_zutat, zutat_2=Italienisches_Essen.default_zutat, zutat_3=Italienisches_Essen.default_zutat, sauce=Italienisches_Essen.default_sauce, scharf=Italienisches_Essen.scharf, extrakaese=Italienisches_Essen.extrakaese):
        """
        Konstruktor der Klasse Pizza.

        Args:
            anzahl (int): Anzahl der Pizzas.
            zutat_1, zutat_2, zutat_3 (str): Zutaten für die Pizza.
            sauce (str): Sauce für die Pizza.
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
        Bereitet die Pizza zu und speichert die Beschreibung der Zubereitung.
        """
     
        plural = "Pizzen" if self.anzahl > 1 else "Pizza"
        extras = []
        if self.scharf:
            extras.append("Zusätzlich scharf gewürzt")
        if self.extrakaese:
            extras.append("mit extra Käse")

        extras_str = " und ".join(extras)
        self.zubereitungsdetails = (f"{self.anzahl}x {plural} mit den Zutaten: {self.zutat_1}, {self.zutat_2}, {self.zutat_3}. "
                                    f"Sauce: {self.default_sauce}. {extras_str}")
    def __str__(self):
        """
        Gibt die finale Beschreibung der Pizza zurück, inklusive der Zubereitungsdetails.
        """
        return self.zubereitungsdetails
