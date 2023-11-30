class Pasta():
    """
        Klasse, die eine Pasta darstellt.

        Klassenattribute:
            pastaAnzahl (int): Gesamtanzahl der Pasta
            defaultSauce (str): Standardsauce für alle Pasta

        Attribute:
            zutat_1 (str): Erste Zutat
            zutat_2 (str): Zweite Zutat
            zutat_3 (str): Dritte Zutat

        Methoden:
            __init__: Konstruktor, der eine neue Pasta erstellt
            pasta_belegen: Ändert die Zutaten der Pasta
            __str__(): Gibt eine Beschreibung der Pasta zurück.
    """
    pastaAnzahl = 0
    defaultPasta = "Spagetti"
    defaultSauce = "Hackfleischsoße"
    defaultKaeseUeberbacken = False


    def __init__(self, xxx):
        """
        Initialisierung der Pasta
            Args:
                zutat_1 (str): Erste Zutat
                zutat_2 (str): Zweite Zutat
                zutat_3 (str): Dritte Zutat
        """
        # self.zutat_1 = zutat_1
        # self.zutat_2 = zutat_2
        # self.zutat_3 = zutat_3
        # Pasta.pastaAnzahl += 1

    def pasta_zusammenstellen(self, xxx):
        """
        Stellt Pasta mit Soße zusammen
            Args:
                z_1 (str): Erste neue Zutat
                z_2 (str): Zweite neue Zutat
                z_3 (str): Dritte neue Zutat
        """
        # self.zutat_1 = z_1
        # self.zutat_2 = z_2
        # self.zutat_3 = z_3

    def __str__(self):
        """
        Gibt eine Beschreibung der Pasta zurück.

        Returns:
            str: Beschreibung der Pasta, einschließlich Zutaten, Standardsoße und Gesamtanzahl der Pizzas.
        """
        return f"Pasta mit {self.zutat_1}, {self.zutat_2}, {self.zutat_3}. Standardsoße: {Pasta.defaultSauce}. Gesamtanzahl Pizzen: {Pasta.pastaAnzahl}"