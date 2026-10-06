import numpy as np

class Kunde:
    """
    Modell fuer einen Kunden bei einer Tankstelle
    """
    def __init__(self, wendepunkt:float=0, tankvolumen:int=60, fahrer_geschwindigkeit:int=50):
        self.wendepunkt = wendepunkt # theoretischer Bereitschaftswert. Ein "Give a Fuck" Faktor. Je hoeher desto leichter wechseln die Autofahrer die Tankstelle bei Preisunterschieden
        self.tankvolumen = tankvolumen
        self.fahrer_geschwindigkeit = fahrer_geschwindigkeit

    def aktivierung(self, X, a:float=3.4045, p:float=0.8971):
        """
        Gibt den Anteil der Wechsler für einen Interessewert an. Funktion basiert auf der Einkommensverteilung in Deutschland
        """
        if self.wendepunkt == 0:
            return 1
        b = 1.046*self.wendepunkt
        anteil = (1 + (X/b) ** -a) ** -p
        return anteil

    def ersparnis_pro_weg(self, Tankstelle_Start, Tankstelle_Ziel):
        return 0.1 * ( self.tankvolumen * np.abs(Tankstelle_Start.preis - Tankstelle_Ziel.preis) ) / ( Tankstelle_Ziel.distanz / self.fahrer_geschwindigkeit ) # EUR/h
        

class Tankstelle:
    def __init__(self, preis:int, distanz:int=0):
        self.preis = preis # EUR/L
        self.distanz = distanz # Kilometer vom Ortnullpunkt

    #Optimale Preise fuer maximales profit_volumen()
    def preis_anpassen():
        # """ mogliche Parameter: Maximaler preissprung, Konkurrenz Tankstelle, aktivierungsfunktion der Kunden"""
        return 0

    # Funktion mit Margin, Einkaufspreis, Anteil an Kunden vom Pool
    def profit_volumen():
        return 0


# Implement Class for Verkehrflow
# in order to simulate changing global environments
# Sprung, 