import numpy as np

class Kunde:
    """
    Modell fuer einen Kunden bei einer Tankstelle
    """
    def __init__(self, wendepunkt:float=0, tankvolumen:int=60, fahrer_geschwindigkeit:int=30):
        # wendepunkt := Bereitschaftswert. Ein "Give a Fuck" Faktor. 
        # Je hoeher desto leichter wechseln die Autofahrer die Tankstelle bei Preisunterschieden
        # Einheit ist Ersparnis pro stunde in EUR/h
        self.wendepunkt = wendepunkt 
        self.tankvolumen = tankvolumen
        self.fahrer_geschwindigkeit = fahrer_geschwindigkeit

    def aktivierung(self, X, uhrzeit:float = 12):
        """
        Gibt den Anteil der Wechsler für einen Interessewert (Ersparnis pro weg)
        an. Funktion basiert auf der Einkommensverteilung in Deutschland
        """
        a:float=3.4045
        p:float=0.8971
        if X <= 0:
            return 0
        if self.wendepunkt == 0:
            return 1
        b = 1.046* self.wendepunkt * self.stress_funktion(uhrzeit)
        anteil = (1 + (X/b) ** -a) ** -p
        return anteil

    def ersparnis_pro_weg(self, Tankstelle_Start, Tankstelle_Ziel, abstand:int = 1):
        return 0.01 * ( self.tankvolumen * (Tankstelle_Start.verkaufs_preis - Tankstelle_Ziel.verkaufs_preis) ) / ( abstand / self.fahrer_geschwindigkeit ) # EUR/h
    
    def stress_funktion(self, stunde:int=12):
        # 24-Stunden-Periodizität
        x24 = stunde % 24

        # bisherige Tagesfunktion
        f = (
           27 * np.exp(-((x24 - 7.5) / 2)**2)
            + 8 * np.exp(-((x24 - 12.5) / 3)**2)
            + 19 * np.exp(-((x24 - 17.5) / 2.3)**2)
        ) / 27

        # Sinusfunktion
        s = np.sin(2 * np.pi * stunde / 24 - 2 * np.pi) + 1

        # miteinander verrechnen
        stress_faktor = f * s
        return stress_faktor


class Tankstelle:
    def __init__(self, preis:int, einkaufs_preis:float = 70, energie_steuer:int = 65, co_2_abgabe:float = 17, mehrwert_steuer:float=0.19):
        self.verkaufs_preis = preis # EUR/L
        self.einkaufs_preis = einkaufs_preis # cents
        self.energie_steuer = energie_steuer # cents
        self.co_2_abgabe = co_2_abgabe # cents
        self.mehrwert_steuer = mehrwert_steuer # anteil

    #Optimale Preise fuer maximales profit_volumen()
    def preis_anpassen(self):
        # """ mogliche Parameter: Maximaler preissprung, Konkurrenz Tankstelle, aktivierungsfunktion der Kunden"""
        verkaufs_preis_optimal = 1
        return verkaufs_preis_optimal

    # Funktion mit Margin, Einkaufspreis, Anteil an Kunden vom Pool
    def profit_volumen(self, kundschaft:float=1):
        margin = (self.verkaufs_preis - self.einkaufs_preis)/(1+self.mehrwert_steuer) - self.co_2_abgabe - self.energie_steuer # cent pro Liter Gewinn
        return kundschaft * margin



def profit_volumen_auswerten(kunde, tankstelle_A, tankstelle_B, tankstelle_C,
                             uhrzeit:int = 12, 
                             app_nutzer_anteil:float = 1.0,
                             abstand_AB:float = 1,
                             abstand_BC:float = 1,
                             abstand_AC:float = 1,
                             fluss_A:float = 1,
                             fluss_B:float = 1,
                             fluss_C:float = 1,
                             verbose:bool = False
                             ):
    """
    Betrachtet die, oh wehe es ist fertig!
    """
    
    if abstand_AB  == 0 or abstand_BC == 0 or abstand_AC == 0:
        print("Divison by Zero!!!")
        return 0, 0, 0

    ersparnis_AB = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_A, Tankstelle_Ziel=tankstelle_B, abstand=abstand_AB)
    ersparnis_BA = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_B, Tankstelle_Ziel=tankstelle_A, abstand=abstand_AB)
    ersparnis_AC = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_A, Tankstelle_Ziel=tankstelle_C, abstand=abstand_AC)
    ersparnis_BC = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_B, Tankstelle_Ziel=tankstelle_C, abstand=abstand_BC)
    ersparnis_CA = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_C, Tankstelle_Ziel=tankstelle_A, abstand=abstand_AC)
    ersparnis_CB = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_C, Tankstelle_Ziel=tankstelle_B, abstand=abstand_BC)

    aktivierung_AB = kunde.aktivierung(X=ersparnis_AB, uhrzeit=uhrzeit)
    aktivierung_BA = kunde.aktivierung(X=ersparnis_BA, uhrzeit=uhrzeit)
    aktivierung_BC = kunde.aktivierung(X=ersparnis_BC, uhrzeit=uhrzeit)
    aktivierung_AC = kunde.aktivierung(X=ersparnis_AC, uhrzeit=uhrzeit)
    aktivierung_CA = kunde.aktivierung(X=ersparnis_CA, uhrzeit=uhrzeit)
    aktivierung_CB = kunde.aktivierung(X=ersparnis_CB, uhrzeit=uhrzeit)

    # Berechnung der Wechselwahrscheinlichkeiten, avoids total values over 
    if aktivierung_AB > aktivierung_AC:
        wechsel_A_nach_B = aktivierung_AB * fluss_A
        wechsel_A_nach_C = 0
    elif aktivierung_AB < aktivierung_AC:
        wechsel_A_nach_B = aktivierung_AB * fluss_A * (1 - app_nutzer_anteil)
        wechsel_A_nach_C = aktivierung_AC * fluss_A * app_nutzer_anteil
    else:
        wechsel_A_nach_B = 0.5 * aktivierung_AB * fluss_A * app_nutzer_anteil + aktivierung_AB * fluss_A * (1 - app_nutzer_anteil)
        wechsel_A_nach_C = 0.5 * aktivierung_AC * fluss_A * app_nutzer_anteil

    if aktivierung_BA > aktivierung_BC:
        wechsel_B_nach_A = aktivierung_BA * fluss_B
        wechsel_B_nach_C = 0
    elif aktivierung_BA < aktivierung_BC:
        wechsel_B_nach_A = aktivierung_BA * fluss_B * (1 - app_nutzer_anteil)
        wechsel_B_nach_C = aktivierung_BC * fluss_B * app_nutzer_anteil
    else:
        wechsel_B_nach_A = 0.5 * aktivierung_BA * fluss_B * app_nutzer_anteil + aktivierung_BA * fluss_B * (1 - app_nutzer_anteil)
        wechsel_B_nach_C = 0.5 * aktivierung_BC * fluss_B * app_nutzer_anteil

    if aktivierung_CA > aktivierung_CB:
        wechsel_C_nach_A = aktivierung_CA * fluss_C * app_nutzer_anteil
        wechsel_C_nach_B = 0
    elif aktivierung_CA < aktivierung_CB:
        wechsel_C_nach_A = 0
        wechsel_C_nach_B = aktivierung_CB * fluss_C * app_nutzer_anteil
    else:
        wechsel_C_nach_A = 0.5 * aktivierung_CA * fluss_C * app_nutzer_anteil
        wechsel_C_nach_B = 0.5 * aktivierung_CB * fluss_C * app_nutzer_anteil

    # Berechnung der Kundschaft für jede Tankstelle
    kundschaft_A = fluss_A - wechsel_A_nach_B - wechsel_A_nach_C + wechsel_B_nach_A + wechsel_C_nach_A
    kundschaft_B = fluss_B - wechsel_B_nach_A - wechsel_B_nach_C + wechsel_A_nach_B + wechsel_C_nach_B
    kundschaft_C = fluss_C - wechsel_C_nach_A - wechsel_C_nach_B + wechsel_A_nach_C + wechsel_B_nach_C

    #Check for validity of flow dynamics
    total_kundschaft = kundschaft_A + kundschaft_B + kundschaft_C
    total_fluss = fluss_A + fluss_B + fluss_C
    if total_kundschaft != total_fluss:
        print("something aint right")

    # Calling the profit volume calculator for the customers
    profit_volumen_A = tankstelle_A.profit_volumen(kundschaft=kundschaft_A)
    profit_volumen_B = tankstelle_B.profit_volumen(kundschaft=kundschaft_B)
    profit_volumen_C = tankstelle_C.profit_volumen(kundschaft=kundschaft_C)

    if verbose == True:
        print("\n=== INFORMATION TANKSTELLE VERGLEICH ===")

        print("Abstand A und B:", abstand_AB)
        print("Abstand B und C:", abstand_BC)
        print("Abstand C und A:", abstand_AC)

        print("======")

        print("Fluss A", fluss_A)
        print("Fluss B", fluss_B)
        print("Fluss C", fluss_C)

        print("======")

        print("Preis Tankstelle A: ", tankstelle_A.verkaufs_preis, "Cent")
        print("Preis Tankstelle B: ", tankstelle_B.verkaufs_preis, "Cent")
        print("Preis Tankstelle C: ", tankstelle_C.verkaufs_preis, "Cent")

        print("=======")

        print("Uhrzeit: ", uhrzeit)
        print("App Nutzer Anteil: ", app_nutzer_anteil)

        print("=======")

        print("Ersparnis von A nach B: ", ersparnis_AB, "EUR/h")
        print("Ersparnis von A nach C: ", ersparnis_AC, "EUR/h")
        print("Ersparnis von B nach A: ", ersparnis_BA, "EUR/h")
        print("Ersparnis von B nach C: ", ersparnis_BC, "EUR/h")
        print("Ersparnis von C nach A: ", ersparnis_CA, "EUR/h")
        print("Ersparnis von C nach B: ", ersparnis_CB, "EUR/h")

        print("=======")

        print("Kundschaft Gesamt: ", kundschaft_A + kundschaft_B + kundschaft_C)
        print("Kundschaft der Tankstelle A: ", kundschaft_A)
        print("Kundschaft der Tankstelle B: ", kundschaft_B)
        print("Kundschaft der Tankstelle C: ", kundschaft_C)

        print("=======")

        print("Profit Volumen Tankstelle A", profit_volumen_A) 
        print("Profit Volumen Tankstelle B", profit_volumen_B)
        print("Profit Volumen Tankstelle C", profit_volumen_C)
        print("=== END OF PROTOCOL ===\n\n")

    # Returns a list of np.float profit_volumes
    return profit_volumen_A, profit_volumen_B, profit_volumen_C