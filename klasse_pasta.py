from oberklasse_italienisches_essen import Italienisches_Essen

class Pasta(Italienisches_Essen):
    """
    Klasse, die ein Pastagericht darstellt.
    Diese Klasse erbt von Italienisches_Essen und implementiert die spezifischen Eigenschaften einer Pizza.
    """

    def __init__(self, datenbank):
        """
        Initialisiert eine Instanz der Pasta-Klasse mit einer Datenbank.

        Args:
            datenbank (dict): Eine Datenbank mit Zutaten und ihren Preisen.
        """
        super().__init__(datenbank)

    def waehle_option(self):
        """
        Ermöglicht dem Benutzer die Auswahl der Pastasorte.
        """
        return self.erfasse_optionen(self.datenbank['dict_pasta_sorte'])

    def essen_kochen(self, zutaten):
        """
        Stellt die Pasta zusammen, indem die ausgewählten Zutaten verarbeitet werden.
        Die erste Zutat wird als die gewählte Pastasorte betrachtet. Die weiteren Zutaten
        werden zur Liste der Zutaten hinzugefügt, und die Zubereitungsdetails werden entsprechend aktualisiert.

        Args:
            zutaten (dict): Ein Dictionary von ausgewählten Zutaten für die Pasta und ihren Preisen. 
                            Die erste Zutat wird als die gewählte Pizza-Größe betrachtet.
        """
        self.zutaten = zutaten
        pastasorte = next(iter(zutaten.keys()))
        self.zubereitungsdetails = f"{pastasorte} mit " + ', '.join(list(zutaten.keys())[1:])