from classes.oberklasse_italienische_getränke import Italienische_Getraenke

class Getraenke(Italienische_Getraenke):
    """
    Klasse, die ein Getränk repräsentiert.
    """

    def __init__(self, datenbank):
        super().__init__(datenbank)

    def waehle_option(self):
        """
        Ermöglicht dem Benutzer die Auswahl zwischen kalten und heißen Getränken.
        """
        getraenketyp = input("Wählen Sie die Art des Getränks (01: Kaltgetränke, 02: Heißgetränke): ")
        if getraenketyp == "01":
            return self.erfasse_optionen('dict_kaltgetraenke')
        elif getraenketyp == "02":
            return self.erfasse_optionen('dict_heissgetraenke')
        else:
            print("Ungültige Auswahl. Bitte wählen Sie '01' für Kaltgetränke oder '02' für Heißgetränke.")
            return self.waehle_option()

    def getraenk_zubereiten(self, auswahl):
        """
        Stellt das Getränk zusammen, basierend auf der Benutzerauswahl.
        """
        self.zutaten = auswahl
        getraenk_name = next(iter(auswahl.keys()))
        self.zubereitungsdetails = f"Ihr gewähltes Getränk: {getraenk_name}"
        print(self.zubereitungsdetails)

