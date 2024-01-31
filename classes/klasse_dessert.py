from classes.oberklasse_italienisches_restaurant import Italienisches_Restaurant

class Dessert(Italienisches_Restaurant):
    def __init__(self, datenbank):
        super().__init__(datenbank)

    def waehle_option(self):
        geschmacksrichtungen = self.erfasse_optionen('dict_geschmack', mehrfachauswahl=True)
        eissorte = self.erfasse_optionen('dict_eis_sorten', mehrfachauswahl=False)
        return ({**geschmacksrichtungen, **eissorte}, [])

    def bestellung_abschließen(self, zutaten):
        self.zutaten = zutaten
        eis_sorte = next(iter(zutaten.keys()))
        self.zubereitungsdetails = f"Eis ({eis_sorte}) als " + ', '.join(list(zutaten.keys())[1:])