from classes.oberklasse_italienisches_essen import Italienisches_Essen

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
        Ermöglicht dem Benutzer die Auswahl der Größe der Pizza. Diese Methode ruft 'erfasse_optionen' auf, um dem 
        Benutzer eine Auswahl an verschiedenen Pizzagrößen anzubieten, die in der Datenbank unter 'dict_pizza_groesse' 
        definiert sind.

        Die Methode gibt das ausgewählte Element zurück, welches die gewählte Pizzagröße und den dazugehörigen Preis 
        enthält. Dies ist eine spezifische Implementierung der abstrakten Methode 'waehle_option' für die Pizza-Klasse.

        Returns:
            dict: Ein Dictionary, das die vom Benutzer ausgewählte Pizzagröße und deren Preis enthält. 
            Das Dictionary enthält genau einen Eintrag mit der Beschreibung der Größe als Schlüssel und dem Preis als Wert.
        """
        return self.erfasse_optionen('dict_pizza_groesse')

    def essen_kochen(self, zutaten):
        """
        Stellt die Pizza zusammen, indem die ausgewählten Zutaten für das Gericht verarbeitet werden. 
        Diese Methode setzt die ausgewählte Pizzagröße und die weiteren Zutaten zusammen, um die 
        endgültigen Zubereitungsdetails für die Pizza zu definieren.

        Die ausgewählten Zutaten werden in einem Dictionary übergeben, wobei die erste Zutat als 
        Pizzagröße betrachtet wird. Die weiteren Einträge im Dictionary repräsentieren zusätzliche 
        Zutaten für die Pizza. Die Methode aktualisiert die internen Attribute der Klasse zur 
        Speicherung der gesamten Zutatenliste und der Zubereitungsdetails.

        Args:
            zutaten (dict): Ein Dictionary von ausgewählten Zutaten für die Pizza. Jeder Eintrag im 
                            Dictionary repräsentiert eine Zutat mit ihrem Namen als Schlüssel und ihrem 
                            Preis als Wert. Der erste Eintrag wird als die gewählte Pizzagröße betrachtet.

        Returns:
            None: Diese Methode gibt keinen Wert zurück, sondern aktualisiert die internen Attribute 
                der Klasse bezüglich der Zutaten und Zubereitungsdetails.
        """
        self.zutaten = zutaten
        pizza_groesse = next(iter(zutaten.keys()))
        self.zubereitungsdetails = f"Pizza ({pizza_groesse}) mit " + ', '.join(list(zutaten.keys())[1:])