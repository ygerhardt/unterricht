class Pizza():
    """
        Klasse, die eine Pizza darstellt.

        Klassenattribute:
            pizzaAnzahl (int): Gesamtanzahl der Pizzen
            defaultSauce (str): Standardsauce für alle Pizzen

        Attribute:
            zutat_1 (str): Erste Zutat
            zutat_2 (str): Zweite Zutat
            zutat_3 (str): Dritte Zutat

        Methoden:
            __init__: Konstruktor, der eine neue Pizza erstellt
            pizza_belegen: Ändert die Zutaten der Pizza
            __str__(): Gibt eine Beschreibung der Pizza zurück.
    """
    pizzaAnzahl = 0
    defaultSauce = "Tomaten"

    def __init__(self, zutat_1, zutat_2, zutat_3):
        """
        Initialisierung der Pizza
            Args:
                zutat_1 (str): Erste Zutat
                zutat_2 (str): Zweite Zutat
                zutat_3 (str): Dritte Zutat
        """
        self.zutat_1 = zutat_1
        self.zutat_2 = zutat_2
        self.zutat_3 = zutat_3
        Pizza.pizzaAnzahl += 1

    def pizza_belegen(self, z_1, z_2, z_3):
        """
        Ändert die Zutaten der Pizza.
            Args: 
                z_1 (str): Erste neue Zutat 
                z_2 (str): Zweite neue Zutat
                z_3 (str): Dritte neue Zutat
        """
        self.zutat_1 = z_1
        self.zutat_2 = z_2
        self.zutat_3 = z_3

    def __str__(self):
        """
        Gibt eine Beschreibung der Pizza zurück.

        Returns:
            str: Beschreibung der Pizza, einschließlich Zutaten, Standardsoße und Gesamtanzahl der Pizzas. 
        """
        return f"Pizza mit {self.zutat_1}, {self.zutat_2}, {self.zutat_3}. Standardsoße: {Pizza.defaultSauce}. Gesamtanzahl Pizzen: {Pizza.pizzaAnzahl}"