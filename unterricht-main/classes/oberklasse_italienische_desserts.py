from abc import ABC, abstractmethod

class ItalienischeDesserts(ABC):
    """
    Abstrakte Oberklasse für italienische Desserts.
    """

    def __init__(self, datenbank):
        """
        Initialisiert ein italienisches Dessert mit einer Datenbank.

        Args:
            datenbank (dict): Eine Datenbank mit Zutaten und ihren Preisen.
        """
        self.datenbank = datenbank
        self.zutaten = {}
        self.zubereitungsdetails = ""

    @abstractmethod
    def dessert_zubereiten(self, geschmack):
        """
        Abstrakte Methode zum Zusammenstellen und Zubereiten des Desserts. Diese Methode soll in jeder Unterklasse
        implementiert werden und ist verantwortlich für die Verarbeitung der ausgewählten Zutaten und die
        Zusammenstellung des Endprodukts.

        In dieser Methode sollten die spezifischen Schritte definiert werden, die notwendig sind, um das
        Dessert basierend auf den ausgewählten Zutaten vorzubereiten. Dazu gehört die Verarbeitung der Zutatenliste,
        die Berechnung des Gesamtpreises und das Festlegen der endgültigen Zubereitungsdetails für das Dessert.

        Args:
            zutaten (dict): Ein Dictionary der ausgewählten Zutaten für das Dessert. Jeder Eintrag im Dictionary
            repräsentiert eine Zutat mit ihrem Namen als Schlüssel und ihrem Preis als Wert. Die Implementierung in
            den Unterklassen kann je nach Art des Desserts variieren und sollte die spezifischen Anforderungen und
            des jeweiligen Desserttyps berücksichtigen.

        Returns:
            None: Diese Methode soll keine Werte zurückgeben, sondern dient dazu, die internen Attribute der Klasse
            (wie die Liste der Zutaten und die Zubereitungsdetails) zu aktualisieren.
        """
        pass

    @abstractmethod
    def waehle_option(self):
        """
        Abstrakte Methode zur Auswahl einer Option für das Dessert. Diese Methode soll in jeder Unterklasse
        implementiert werden und dient dazu, spezifische Optionen für verschiedene Desserttypen zu definieren und zu verarbeiten.

        Die Implementierung in den Unterklassen sollte die Benutzerinteraktion steuern, um eine Auswahl aus den
        verfügbaren Optionen zu treffen, die für den jeweiligen Desserttyp spezifisch sind. Diese Methode wird in Verbindung
        mit 'erfasse_optionen' verwendet, um eine konsistente und benutzerfreundliche Auswahlmöglichkeit zu bieten.

        Returns:
            dict: Ein Dictionary, das die vom Benutzer ausgewählte Option und deren Preis enthält.
        """
        pass

    # Die übrigen Hilfsmethoden (erfasse_optionen und erfasse_bestellung) bleiben unverändert.
    # Sie können je nach Bedarf angepasst werden.
    def erfasse_optionen(self, optionenTyp, mehrfachauswahl=False):
        """
        Erlaubt dem Benutzer, Optionen aus einem Dictionary von Optionen zu wählen.
        Bei 'dict_scharf' und 'dict_extrakaese' wird eine Ja/Nein-Abfrage gestellt, bei allen anderen Optionen ist
        Mehrfachauswahl möglich, und es sind doppelte Optionen nicht erlaubt.

        Args:
            optionenTyp (str): Ein Dictionary von Optionen, aus denen der Benutzer wählen kann.
            mehrfachauswahl (bool): Gibt an, ob Mehrfachauswahl erlaubt ist.

        Returns:
            dict: Ausgewählte Optionen und ihre Preise.
        """
        verfuegbareOptionen = self.datenbank[optionenTyp]
        ausgewaehlteOptionen = {}

        if optionenTyp in ['dict_geschmack', 'dict_sauce']:
            for key, value in verfuegbareOptionen.items():
                while True:
                    auswahl = input(f"Möchten Sie den Geschmack  {value['Beschreibung']} (Preis: {value['Preis']:.2f}\u20AC) hinzufügen? (ja/nein): ").lower()
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

    def erfasse_bestellung(self, hauptkomponente):
        """
        Erfasst eine Bestellung, indem sie die Hauptkomponente (z.B. Art des Desserts),
        Zutaten, Sauce und zusätzliche Optionen wie 'scharf' und 'extra Käse' kombiniert.

        Die Methode ruft andere Hilfsmethoden auf, um die einzelnen Teile der Bestellung zusammenzustellen.
        Anschließend wird die Methode 'dessert_zubereiten' aufgerufen, um die Bestellung zu verarbeiten.

        Args:
            hauptkomponente (dict): Die Hauptkomponente der Bestellung, wie von der spezifischen Unterklasse definiert.
        Returns:
            dict: Die gesamte zusammengestellte Bestellung, einschließlich der Hauptkomponente, Zutaten, Sauce und zusätzlichen Optionen.
        """
        optionenTypen = ['dict_zutaten', 'dict_sauce', 'dict_scharf', 'dict_extrakaese']
        mehrfachauswahl = [True, False, False, False]
        bestellung = {**hauptkomponente}

        for optionenTyp, mehrfach in zip(optionenTypen, mehrfachauswahl):
            bestellung.update(self.erfasse_optionen(optionenTyp, mehrfach))

        self.dessert_zubereiten(bestellung)
        
        return bestellung