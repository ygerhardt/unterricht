from oberklasse_italienisches_essen import Italienisches_Essen

class Pizza(Italienisches_Essen):
    """
    Klasse, die eine Pizza darstellt.
    Diese Klasse erbt von Italienisches_Essen und implementiert die spezifischen Eigenschaften einer Pizza.
    """

    def __init__(self, datenbank):
        """
        Initialisiert eine Pizza mit einer Datenbank.

        Args:
            datenbank (dict): Eine Datenbank mit Zutaten und ihren Preisen.
        """
        super().__init__(datenbank)

    def waehle_option(self):
        """
        Ermöglicht dem Benutzer die Auswahl der Größe der Pizza.
        """
        return self.erfasse_optionen(self.datenbank['dict_pizza_groesse'])

    def essen_kochen(self, zutaten):
        """
        Stellt die Pizza zusammen, indem die ausgewählten Zutaten verarbeitet werden.
        Die erste Zutat wird als die gewählte Pizzagröße betrachtet. Die weiteren Zutaten
        werden zur Liste der Zutaten hinzugefügt, und die Zubereitungsdetails werden entsprechend aktualisiert.

        Args:
            zutaten (dict): Ein Dictionary ausgewählter Zutaten für die Pizza mit ihren jeweiligen Preisen.
                            Die erste Zutat wird als die gewählte Pizza-Größe betrachtet.
        """
        self.zutaten = zutaten
        pizza_groesse = next(iter(zutaten.keys()))
        self.zubereitungsdetails = f"Pizza ({pizza_groesse}) mit " + ', '.join(list(zutaten.keys())[1:])