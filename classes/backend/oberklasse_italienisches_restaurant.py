from abc import ABC, abstractmethod

class Italienisches_Restaurant(ABC):
    def __init__(self, datenbank):
        self.datenbank = datenbank
        self.zutaten = {}
        self.zubereitungsdetails = ""

    @abstractmethod
    def bestellung_abschließen(self, auswahl):
        pass

    @abstractmethod
    def waehle_option(self):
        pass

    def erfasse_optionen(self, optionenTyp, mehrfachauswahl=False):
        verfuegbareOptionen = self.datenbank[optionenTyp]
        ausgewaehlteOptionen = {}

        while True:
            for key, value in verfuegbareOptionen.items():
                print(f"{key}: {value['Beschreibung']} (Preis: {value['Preis']:.2f}\u20AC)")

            eingabe = input("\nBitte wählen Sie eine oder mehrere Optionen (z.B. 01,03,05): " if mehrfachauswahl else "\nBitte wählen Sie eine Option (Nummer): ").split(',')
            print()
            
            eingabe_set = set(eingabe)
            if ('00' in eingabe_set and len(eingabe_set) > 1) or (not mehrfachauswahl and len(eingabe_set) > 1) or (mehrfachauswahl and len(eingabe) != len(eingabe_set)):
                print("\nUngültige Auswahl. Bitte versuchen Sie es erneut.\n")
                continue

            ungültigeAuswahl = False
            for nummer in eingabe:
                nummer = nummer.strip()
                if nummer in verfuegbareOptionen:
                    ausgewaehlteOptionen[verfuegbareOptionen[nummer]['Beschreibung']] = verfuegbareOptionen[nummer]['Preis']
                else:
                    print(f"\nUngültige Auswahl: {nummer}. Bitte versuchen Sie es erneut.\n")
                    ungültigeAuswahl = True
                    break

            if not ungültigeAuswahl:
                break

        return ausgewaehlteOptionen

    def erfasse_bestellung(self):
        bestellung, optionen = self.waehle_option()

        for optionenTyp, mehrfach in optionen:
            ausgewaehlteOptionen = self.erfasse_optionen(optionenTyp, mehrfach)
            bestellung.update(ausgewaehlteOptionen)
        
        self.bestellung_abschließen(bestellung)
        return bestellung