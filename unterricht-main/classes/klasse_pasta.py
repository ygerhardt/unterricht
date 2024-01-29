from classes.oberklasse_italienisches_essen import Italienisches_Essen

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
        Ermöglicht dem Benutzer die Auswahl der Pastasorte. Diese Methode ruft 'erfasse_optionen' auf, um dem 
        Benutzer eine Auswahl an verschiedenen Pastasorten anzubieten, die in der Datenbank unter 'dict_pasta_sorte' 
        definiert sind.

        Die Methode gibt das ausgewählte Element zurück, welches die gewählte Pastasorte und den dazugehörigen Preis 
        enthält. Dies ist eine spezifische Implementierung der abstrakten Methode 'waehle_option' für die Pasta-Klasse.

        Returns:
            dict: Ein Dictionary, das die vom Benutzer ausgewählte Pastasorte und deren Preis enthält. 
            Das Dictionary enthält genau einen Eintrag mit der Beschreibung der Sorte als Schlüssel und dem Preis als Wert.
        """
        return self.erfasse_optionen('dict_pasta_sorte')

    def essen_kochen(self, zutaten):
        """
        Stellt die Pasta zusammen, indem die ausgewählten Zutaten für das Gericht verarbeitet werden. 
        Diese Methode setzt die ausgewählte Pastasorte und die weiteren Zutaten zusammen, um die 
        endgültigen Zubereitungsdetails für das Pastagericht zu definieren.

        Die ausgewählten Zutaten werden in einem Dictionary übergeben, wobei die erste Zutat als 
        Pastasorte betrachtet wird. Die weiteren Einträge im Dictionary repräsentieren zusätzliche 
        Zutaten für die Pasta. Die Methode aktualisiert die internen Attribute der Klasse zur 
        Speicherung der gesamten Zutatenliste und der Zubereitungsdetails.

        Args:
            zutaten (dict): Ein Dictionary von ausgewählten Zutaten für die Pasta. Jeder Eintrag im 
                            Dictionary repräsentiert eine Zutat mit ihrem Namen als Schlüssel und ihrem 
                            Preis als Wert. Der erste Eintrag wird als die gewählte Pastasorte betrachtet.

        Returns:
            None: Diese Methode gibt keinen Wert zurück, sondern aktualisiert die internen Attribute 
                der Klasse bezüglich der Zutaten und Zubereitungsdetails.
        """
        self.zutaten = zutaten
        pastasorte = next(iter(zutaten.keys()))
        self.zubereitungsdetails = f"{pastasorte} mit " + ', '.join(list(zutaten.keys())[1:])