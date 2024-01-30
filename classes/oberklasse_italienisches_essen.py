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
        Abstrakte Methode zum Zusammenstellen und "Kochen" des Essens. Diese Methode soll in jeder Unterklasse 
        implementiert werden und ist verantwortlich für die Verarbeitung der ausgewählten Zutaten und die 
        Zusammenstellung des Endprodukts (z.B. der fertigen Pizza oder Pasta).

        In dieser Methode sollten die spezifischen Schritte definiert werden, die notwendig sind, um das 
        Gericht basierend auf den ausgewählten Zutaten vorzubereiten. Dazu gehört die Verarbeitung der Zutatenliste, 
        die Berechnung des Gesamtpreises und das Festlegen der endgültigen Zubereitungsdetails für das Gericht.

        Args:
            zutaten (dict): Ein Dictionary der ausgewählten Zutaten für das Gericht. Jeder Eintrag im Dictionary 
            repräsentiert eine Zutat mit ihrem Namen als Schlüssel und ihrem Preis als Wert. Die Implementierung in 
            den Unterklassen kann je nach Art des Gerichts variieren und sollte die spezifischen Anforderungen und 
            des jeweiligen Gerichtstyps berücksichtigen.

        Returns:
            None: Diese Methode soll keine Werte zurückgeben, sondern dient dazu, die internen Attribute der Klasse 
            (wie die Liste der Zutaten und die Zubereitungsdetails) zu aktualisieren.
        """
        pass

    @abstractmethod
    def waehle_option(self):
        """
        Abstrakte Methode zur Auswahl einer Option für das Gericht. Diese Methode soll in jeder Unterklasse 
        implementiert werden und dient dazu, spezifische Optionen für verschiedene Gerichtstypen (wie Pizza oder Pasta) 
        zu definieren und zu verarbeiten. 

        Die Implementierung in den Unterklassen sollte die Benutzerinteraktion steuern, um eine Auswahl aus den 
        verfügbaren Optionen zu treffen, die für den jeweiligen Gerichtstyp spezifisch sind (z.B. Pizzagröße oder 
        Pastasorte). Diese Methode wird in Verbindung mit 'erfasse_optionen' verwendet, um eine 
        konsistente und benutzerfreundliche Auswahlmöglichkeit zu bieten.

        Returns:
            dict: Ein Dictionary, das die vom Benutzer ausgewählte Option und deren Preis enthält.
        """
        pass

    def erfasse_optionen(self, optionenTyp, mehrfachauswahl=False):
        """
        Erlaubt dem Benutzer, Optionen aus einem Dictionary von Optionen zu wählen.
        Bei 'dict_zutaten' ist Mehrfachauswahl möglich, bei allen anderen Optionen ist nur eine Einzelauswahl gestattet.
        Bei Mehrfachauswahl sind doppelte Optionen nicht erlaubt. Bei Einzelauswahl muss der Benutzer genau eine Option wählen.
        Bei 'dict_scharf' und 'dict_extrakaese' wird eine Ja/Nein-Abfrage gestellt

        Args:
            optionenTyp (str): Ein Dictionary von Optionen, aus denen der Benutzer wählen kann.
            mehrfachauswahl (bool): Gibt an, ob Mehrfachauswahl erlaubt ist.

        Returns:
            dict: Ausgewählte Optionen und ihre Preise.
        """
        verfuegbareOptionen = self.datenbank[optionenTyp]
        ausgewaehlteOptionen = {}

        if optionenTyp in ['dict_scharf', 'dict_extrakaese']:
            for key, value in verfuegbareOptionen.items():
                while True:
                    auswahl = input(f"Möchten Sie {value['Beschreibung']} (Preis: {value['Preis']:.2f}\u20AC) hinzufügen? (ja/nein): ").lower()
                    if auswahl == 'ja':
                        ausgewaehlteOptionen[value['Beschreibung']] = value['Preis']
                        break
                    elif auswahl == 'nein':
                        break
                    else:
                        print("\nUngültige Eingabe. Bitte antworten Sie mit 'ja' oder 'nein'.\n")
        else:
            while True:
                for key, value in verfuegbareOptionen.items():
                    print(f"{key}: {value['Beschreibung']} (Preis: {value['Preis']:.2f}\u20AC)")

                eingabe = input("\nBitte wählen Sie eine oder mehrere Optionen (z.B. 01,03,05): " if mehrfachauswahl else "\nBitte wählen Sie eine Option (Nummer): ").split(',')

                if not mehrfachauswahl and len(eingabe) > 1:
                    print("\nUngültige Auswahl. Bitte wählen Sie nur eine Option.\n")
                    continue

                if mehrfachauswahl and len(eingabe) != len(set(eingabe)):
                    print("\nDoppelte Optionen sind nicht erlaubt. Bitte versuchen Sie es erneut.\n")
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
        
        optionenTypen = ['dict_zutaten', 'dict_sauce', 'dict_scharf', 'dict_extrakaese']
        mehrfachauswahl = [True, False, False, False]

        bestellung = self.waehle_option()

        for optionenTyp, mehrfach in zip(optionenTypen, mehrfachauswahl):
            bestellung.update(self.erfasse_optionen(optionenTyp, mehrfach))

        self.essen_kochen(bestellung)

        return bestellung