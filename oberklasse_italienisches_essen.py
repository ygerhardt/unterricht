from abc import ABC, abstractmethod

class Italienisches_Essen(ABC):
    """
    Abstrakte Oberklasse für italienische Gerichte.
    """

    def __init__(self, datenbank):
        """
        Initialisiert ein italienisches Essen mit einer Datenbank.

        Args:
            datenbank (dict): Eine Datenbank mit Zutaten und ihren Preisen.
        """
        self.datenbank = datenbank
        self.zutaten = {}
        self.zubereitungsdetails = ""

    @abstractmethod
    def essen_kochen(self, zutaten):
        """
        Abstrakte Methode zum Kochen des Essens.
        Muss in jeder Unterklasse implementiert werden.

        Args:
            zutaten (dict): Ausgewählte Zutaten für das Gericht.
        """
        pass

    def erfasse_optionen(self, verfuegbareOptionen):
        """
        Erlaubt dem Benutzer, Optionen aus einem Dictionary von Optionen zu wählen.
        Bei 'dict_zutaten' ist Mehrfachauswahl möglich, bei allen anderen Optionen nur Einzelauswahl.

        Args:
            verfuegbareOptionen (dict): Ein Dictionary von Optionen, aus denen der Benutzer wählen kann.

        Returns:
            dict: Ausgewählte Optionen und ihre Preise.
        """
        mehrfachauswahl = verfuegbareOptionen is self.datenbank['dict_zutaten']
        ausgewaehlteOptionen = {}

        for key, value in verfuegbareOptionen.items():
            print(f"{key}: {value['Beschreibung']} (Preis: {value['Preis']:.2f}€)")

        eingabe = input("\nBitte wählen Sie eine oder mehrere Optionen (z.B. 01,03,05): " if mehrfachauswahl else "\nBitte wählen Sie eine Option (Nummer): ").split(',')

        for nummer in eingabe:
            nummer = nummer.strip()
            if nummer in verfuegbareOptionen:
                ausgewaehlteOptionen[verfuegbareOptionen[nummer]['Beschreibung']] = verfuegbareOptionen[nummer]['Preis']
                if not mehrfachauswahl:
                    break
            else:
                print(f"\nUngültige Auswahl. Bitte versuchen Sie es erneut.\n")
                return self.erfasse_optionen(verfuegbareOptionen)

        if not ausgewaehlteOptionen:
            print("\nKeine gültigen Optionen ausgewählt. Bitte versuchen Sie es erneut.")
            return self.erfasse_optionen(verfuegbareOptionen)

        return ausgewaehlteOptionen

    def erfasse_zusatzoptionen(self, zusatzOptionenTyp):
        """
        Erfasst zusätzliche Optionen wie 'scharf' und 'extra Käse'.

        Args:
            zusatzOptionenTyp (str): Ein Dictionary von zusätzlichen Optionen, aus denen der Benutzer wählen kann.

        Returns:
            dict: Ausgewählte zusätzliche Optionen und ihre Preise.
        """
        zusatzOptionen = {}
        for _, value in self.datenbank[zusatzOptionenTyp].items():
            while True:
                auswahl = input(f"\nMöchten Sie {value['Beschreibung']} hinzufügen? (ja/nein): ")
                if auswahl.lower() == 'ja':
                    zusatzOptionen[value['Beschreibung']] = value['Preis']
                    break
                elif auswahl.lower() == 'nein':
                    break
                else:
                    print("\nUngültige Auswahl. Bitte geben Sie 'ja' oder 'nein' ein.")
        
        return zusatzOptionen
    
    def erfasse_bestellung(self, hauptkomponente):
        """
        Erfasst eine Bestellung, indem sie die Hauptkomponente (z.B. Größe der Pizza oder Sorte der Pasta),
        Zutaten, Sauce und zusätzliche Optionen wie 'scharf' und 'extra Käse' kombiniert.

        Die Methode ruft andere Hilfsmethoden auf, um die einzelnen Teile der Bestellung zusammenzustellen.
        Anschließend wird die Methode 'essen_kochen' aufgerufen, um die Bestellung zu verarbeiten.

        Args:
            hauptkomponente (dict): Die Hauptkomponente der Bestellung, wie von der spezifischen Unterklasse definiert.
                                    Für Pizza ist dies die Größe, für Pasta die Nudelsorte.
        Returns:
            dict: Die gesamte zusammengestellte Bestellung, einschließlich der Hauptkomponente, Zutaten, Sauce und zusätzlichen Optionen.
        """
        verfuegbareZutaten = self.erfasse_optionen(self.datenbank['dict_zutaten'])
        verfuegbareSaucen = self.erfasse_optionen(self.datenbank['dict_sauce'])
        zusatzScharf = self.erfasse_zusatzoptionen('dict_scharf')
        zusatzKaese = self.erfasse_zusatzoptionen('dict_extrakaese')
        bestellung = {**hauptkomponente, **verfuegbareZutaten, **verfuegbareSaucen, **zusatzScharf, **zusatzKaese}
        self.essen_kochen(bestellung)
        
        return bestellung