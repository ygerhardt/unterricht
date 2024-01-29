from classes.oberklasse_italienische_desserts import ItalienischeDesserts

class Eis(ItalienischeDesserts):
    """
    Klasse, die ein Eis repräsentiert.
    Diese Klasse erbt von ItalienischeDesserts und implementiert die spezifischen Eigenschaften eines Eises.
    """

    def __init__(self, datenbank):
        """
        Initialisiert ein Eis mit einer Datenbank.

        Args:
            datenbank (dict): Eine Datenbank mit Zutaten und ihren Preisen.
        """
        super().__init__(datenbank)

    def waehle_option(self):
        """
        Ermöglicht dem Benutzer die Auswahl der Eissorte. Diese Methode ruft 'erfasse_optionen' auf, um dem 
        Benutzer eine Auswahl an verschiedenen Eissorten anzubieten, die in der Datenbank unter 'dict_eis_sorten' 
        definiert sind.

        Die Methode gibt das ausgewählte Element zurück, welches die gewählte Eissorte und den dazugehörigen Preis 
        enthält. Dies ist eine spezifische Implementierung der abstrakten Methode 'waehle_option' für die Eis-Klasse.

        Returns:
            dict: Ein Dictionary, das die vom Benutzer ausgewählte Eissorte und deren Preis enthält. 
            Das Dictionary enthält genau einen Eintrag mit der Beschreibung der Sorte als Schlüssel und dem Preis als Wert.
        """
        geschmacksrichtungen = self.datenbank['dict_geschmack']
        ausgewaehlter_geschmack = self.erfasse_optionen('dict_geschmack', mehrfachauswahl=False)
        
        return self.erfasse_optionen('dict_eis_sorten')

    def dessert_zubereiten(self, zutaten):
        """
        Stellt das Eis zusammen, indem die ausgewählten Zutaten für das Dessert verarbeitet werden. 
        Diese Methode setzt die ausgewählte Eissorte und die weiteren Zutaten zusammen, um die 
        endgültigen Zubereitungsdetails für das Eis zu definieren.

        Die ausgewählten Zutaten werden in einem Dictionary übergeben, wobei die erste Zutat als 
        Eissorte betrachtet wird. Die weiteren Einträge im Dictionary repräsentieren zusätzliche 
        Zutaten für das Eis. Die Methode aktualisiert die internen Attribute der Klasse zur 
        Speicherung der gesamten Zutatenliste und der Zubereitungsdetails.

        Args:
            zutaten (dict): Ein Dictionary von ausgewählten Zutaten für das Eis. Jeder Eintrag im 
                            Dictionary repräsentiert eine Zutat mit ihrem Namen als Schlüssel und ihrem 
                            Preis als Wert. Der erste Eintrag wird als die gewählte Eissorte betrachtet.

        Returns:
            None: Diese Methode gibt keinen Wert zurück, sondern aktualisiert die internen Attribute 
                der Klasse bezüglich der Zutaten und Zubereitungsdetails.
        """
        self.zutaten = zutaten
        eis_sorte = next(iter(zutaten.keys()))
        self.zubereitungsdetails = f"Eis ({eis_sorte}) mit " + ', '.join(list(zutaten.keys())[1:])