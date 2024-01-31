from classes.oberklasse_italienisches_restaurant import Italienisches_Restaurant

class Speisen(Italienisches_Restaurant):
    def __init__(self, datenbank, gericht_typ):
        super().__init__(datenbank)
        self.gericht_typ = gericht_typ

    def waehle_option(self):
        gemeinsame_optionen = [('dict_zutaten', True), ('dict_sauce', False), ('dict_zusatzoptionen', True)]
        if self.gericht_typ == 'Pizza':
            return self.erfasse_optionen('dict_pizza_groesse'), gemeinsame_optionen
        elif self.gericht_typ == 'Pasta':
            return self.erfasse_optionen('dict_pasta_sorte'), gemeinsame_optionen

    def bestellung_abschließen(self, zutaten):
        self.zutaten = zutaten
        hauptkomponente = next(iter(zutaten.keys()))
        if self.gericht_typ == 'Pizza' or self.gericht_typ == 'Pasta':
            self.zubereitungsdetails = f"{hauptkomponente} mit " + ', '.join(list(zutaten.keys())[1:])