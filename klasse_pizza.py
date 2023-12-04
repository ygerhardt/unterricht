class Pizza:
    pizzaAnzahl = 0
    gueltigeZutaten = ["Salami", "Pilze", "Hackfleisch", "Schinken", "Paprika", "Oliven"]
    gueltigeSaucen = ["Tomaten", "Barbecue", "Creme Fraiche"]  

    def __init__(self, zutat_1, zutat_2, zutat_3, sauce="Tomaten"):
        """
        Initialisierung der Pizza.

        Args:
            zutat_1 (str): Erste Zutat.
            zutat_2 (str): Zweite Zutat.
            zutat_3 (str): Dritte Zutat.
            sauce (str): Art der Sauce, standardmäßig Tomatensauce.
        """
        self.setze_zutaten(zutat_1, zutat_2, zutat_3)
        self.setze_sauce(sauce)
        Pizza.pizzaAnzahl += 1

    def setze_zutaten(self, z_1, z_2, z_3):
        """
        Setzt und validiert die Zutaten der Pizza.

        Args:
            z_1 (str): Erste Zutat.
            z_2 (str): Zweite Zutat.
            z_3 (str): Dritte Zutat.
        """
        if z_1 not in Pizza.gueltigeZutaten or z_2 not in Pizza.gueltigeZutaten or z_3 not in Pizza.gueltigeZutaten:
            raise ValueError("Eine oder mehrere Zutaten sind nicht gültig.")
        self.zutat_1 = z_1
        self.zutat_2 = z_2
        self.zutat_3 = z_3

    def setze_sauce(self, sauce):
        """
        Setzt und validiert die Sauce der Pizza.

        Args:
            sauce (str): Art der Sauce.
        """
        if sauce not in Pizza.gueltigeSaucen:
            raise ValueError("Ungültige Sauce.")
        self.sauce = sauce

    def pizza_belegen(self, z_1, z_2, z_3, sauce=None):
        """
        Ändert die Zutaten und ggf. die Sauce der Pizza.

        Args:
            z_1 (str): Erste neue Zutat.
            z_2 (str): Zweite neue Zutat.
            z_3 (str): Dritte neue Zutat.
            sauce (str): Neue Sauce, falls angegeben.
        """
        self.setze_zutaten(z_1, z_2, z_3)
        if sauce:
            self.setze_sauce(sauce)

    def __str__(self):
        """
        Gibt eine Beschreibung der Pizza zurück.

        Returns:
            str: Beschreibung der Pizza, einschließlich Zutaten, Standardsoße und Gesamtanzahl der Pizzas. 
        """
        return f"Pizza mit {self.zutat_1}, {self.zutat_2}, {self.zutat_3}. Sauce: {self.sauce}. Gesamtanzahl Pizzen: {Pizza.pizzaAnzahl}"

