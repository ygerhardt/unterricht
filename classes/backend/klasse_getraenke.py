from classes.backend.oberklasse_italienisches_restaurant import Italienisches_Restaurant

class Getraenke(Italienisches_Restaurant):
    def __init__(self, datenbank):
        super().__init__(datenbank)

    def waehle_option(self):
        getraenketyp = input("Wählen Sie die Art des Getränks (01: Kaltgetränke, 02: Heißgetränke): ")
        if getraenketyp == "01":
            auswahl = self.erfasse_optionen('dict_kaltgetraenke', False)
        elif getraenketyp == "02":
            auswahl = self.erfasse_optionen('dict_heissgetraenke', False)
        else:
            print("Ungültige Auswahl. Bitte wählen Sie '01' für Kaltgetränke oder '02' für Heißgetränke.")
            return self.waehle_option()

        return (auswahl, []) 

    def bestellung_abschließen(self, auswahl):
        self.zutaten = auswahl
        getraenk_name = next(iter(auswahl.keys()))
        self.zubereitungsdetails = f"Ihr gewähltes Getränk: {getraenk_name}"

