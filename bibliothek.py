import numpy as np
import matplotlib.pyplot as plt


# Klasse fuer verschiedene Kundentypen
class Kunde:
    def __init__(self, wendepunkt, tankvolumen=60, fahrer_geschwindigkeit=50):
        self.wendepunkt = wendepunkt #
        self.tankvolumen = tankvolumen
        self.fahrer_geschwindigkeit = fahrer_geschwindigkeit

    # gibt den Anteil der Wechsler für einen Interessewert an. Funktion basiert auf der Einkommensverteilung in Deutschland
    def aktivierung(self, X, a=3.4045, p=0.8971):
        if self.wendepunkt == 0:
            return 1
        b = 1.046*self.wendepunkt
        anteil = (1 + (X/b) ** -a) ** -p
        return anteil

    def ersparnis_pro_weg(self, Tankstelle_Start, Tankstelle_Ziel):
        return 0.1 * ( self.tankvolumen * np.abs(Tankstelle_Start.preis - Tankstelle_Ziel.preis) ) / ( Tankstelle_Ziel.distanz / self.fahrer_geschwindigkeit ) # EUR/h
        

class Tankstelle:
    def __init__(self, preis, distanz=0):
        self.preis = preis # EUR/L
        self.distanz = distanz # Kilometer vom Ortnullpunkt

    def preis_anpassen():
        return 0

    def profit_volumen():
        return 0


