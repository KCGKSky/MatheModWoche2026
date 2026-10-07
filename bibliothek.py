import numpy as np
import config as config

class Kunde:
    """
    Modell fuer einen Kunden bei einer Tankstelle
    """
    def __init__(self, wendepunkt:float=0,  quote:float = 0, tankvolumen:int=config.tankvolumen, fahrer_geschwindigkeit:int=config.fahrer_geschwindigkeit,):
        # wendepunkt := Bereitschaftswert. Ein "Give a Fuck" Faktor.
        # Je hoeher desto leichter wechseln die Autofahrer die Tankstelle bei Preisunterschieden
        # Einheit ist Ersparnis pro stunde in EUR/h
        self.wendepunkt = wendepunkt 
        self.tankvolumen = tankvolumen
        self.fahrer_geschwindigkeit = fahrer_geschwindigkeit
        self.quote = quote

    def aktivierung(self, X, uhrzeit:float = config.uhrzeit):
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
        return 0.01 * ( self.tankvolumen * (Tankstelle_Start.preis_verkauf - Tankstelle_Ziel.preis_verkauf) ) / ( abstand / self.fahrer_geschwindigkeit ) # EUR/h
    
    def stress_funktion(self, uhrzeit:int=config.uhrzeit):
        # 24-Stunden-Periodizität
        x24 = uhrzeit % 24

        # bisherige Tagesfunktion
        f = (
           27 * np.exp(-((x24 - 7.5) / 2)**2)
            + 8 * np.exp(-((x24 - 12.5) / 3)**2)
            + 19 * np.exp(-((x24 - 17.5) / 2.3)**2)
        ) / 27

        # Sinusfunktion
        s = np.sin(2 * np.pi * uhrzeit / 24 - 2 * np.pi) + 1

        # miteinander verrechnen
        stress_faktor = f * s
        return stress_faktor


class Tankstelle:
    def __init__(self, preis_verkauf:int, preis_einkauf:float, energie_steuer:int = config.energie_steuer, co_2_abgabe:float = config.co_2_abgabe, mehrwert_steuer:float=config.mehrwert_steuer):
        self.preis_verkauf = preis_verkauf # EUR/L
        self.preis_einkauf = preis_einkauf # cents
        self.energie_steuer = energie_steuer # cents
        self.co_2_abgabe = co_2_abgabe # cents
        self.mehrwert_steuer = mehrwert_steuer # anteil

    # Funktion mit Margin, Einkaufspreis, Anteil an Kunden vom Pool
    def gewinn_erwartung(self, kundschaft:float=1, tankvolumen=config.tankvolumen, verkehr=config.verkehr):
        margin = (self.preis_verkauf - self.preis_einkauf)/(1+self.mehrwert_steuer) - self.co_2_abgabe - self.energie_steuer # cent pro Liter Gewinn
        return 0.01 * tankvolumen * verkehr * kundschaft * margin



def profit_volumen(kunde, tankstelle_A, tankstelle_B, tankstelle_C,
                             uhrzeit:int = config.uhrzeit,
                             app_nutzer_anteil:float = config.app_nutzer_anteil,
                             verkehr = config.verkehr,
                             abstand_AB:float = config.abstand_AB,
                             abstand_BC:float = config.abstand_BC,
                             abstand_AC:float = config.abstand_AC,
                             fluss_A:float = config.fluss_A,
                             fluss_B:float = config.fluss_B,
                             fluss_C:float = config.fluss_C,
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
    if np.abs(total_kundschaft - total_fluss) > 10**-7:
        print("something aint right")

    # Calling the gewinn_erwartung calculator for the customers
    profit_volumen_A = tankstelle_A.gewinn_erwartung(kundschaft=kundschaft_A, verkehr=verkehr)
    profit_volumen_B = tankstelle_B.gewinn_erwartung(kundschaft=kundschaft_B, verkehr=verkehr)
    profit_volumen_C = tankstelle_C.gewinn_erwartung(kundschaft=kundschaft_C, verkehr=verkehr)

    if verbose == True:
        print("\n=== INFORMATION TANKSTELLE VERGLEICH ===")

        print("Abstand A und B:", abstand_AB)
        print("Abstand B und C:", abstand_BC)
        print("Abstand C und A:", abstand_AC)

        print("======")

        print("Fluss A: ", fluss_A)
        print("Fluss B: ", fluss_B)
        print("Fluss C: ", fluss_C)

        print("======")

        print("Preis Tankstelle A: ", tankstelle_A.preis_verkauf, "Cent")
        print("Preis Tankstelle B: ", tankstelle_B.preis_verkauf, "Cent")
        print("Preis Tankstelle C: ", tankstelle_C.preis_verkauf, "Cent")

        print("=======")

        print("Uhrzeit: ", uhrzeit)
        print("App Nutzer Anteil: ", app_nutzer_anteil)
        print("Verkehrteilnehmer:", verkehr)
        print("Wendepunkt Kunde:", kunde.wendepunkt)
        print("Quote Kunde:", kunde.quote)

        print("=======")

        print("Ersparnis von A nach B: ", ersparnis_AB, "EUR/h")
        print("Ersparnis von A nach C: ", ersparnis_AC, "EUR/h")
        print("Ersparnis von B nach A: ", ersparnis_BA, "EUR/h")
        print("Ersparnis von B nach C: ", ersparnis_BC, "EUR/h")
        print("Ersparnis von C nach A: ", ersparnis_CA, "EUR/h")
        print("Ersparnis von C nach B: ", ersparnis_CB, "EUR/h")

        print("=======")

        print("Wechsler Fluss von A nach B: ", wechsel_A_nach_B)
        print("Wechsler Fluss von A nach C: ", wechsel_A_nach_C)
        print("Wechsler Fluss von B nach A: ", wechsel_B_nach_A)
        print("Wechsler Fluss von B nach C: ", wechsel_B_nach_C)
        print("Wechsler Fluss von C nach A: ", wechsel_C_nach_A)
        print("Wechsler Fluss von C nach B: ", wechsel_C_nach_B)

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

def gesamt_profit_volumen(kunden:list, tankstelle_A, tankstelle_B, tankstelle_C,
                            uhrzeit:int = config.uhrzeit,
                            app_nutzer_anteil:float = config.app_nutzer_anteil,
                            verkehr = config.verkehr,
                            abstand_AB:float = config.abstand_AB,
                            abstand_BC:float = config.abstand_BC,
                            abstand_AC:float = config.abstand_AC,
                            fluss_A:float = config.fluss_A,
                            fluss_B:float = config.fluss_B,
                            fluss_C:float = config.fluss_C,
                            verbose:bool = config.verbose_value
                                                         ):
    """
    Berechnet das Gesamtprofit-Volumen für eine Liste von Kunden.
    """
    gesamt = [0, 0, 0]  # [profit_A, profit_B, profit_C]
    for kunde in kunden:
        profit = profit_volumen(kunde=kunde,
                                tankstelle_A=tankstelle_A,
                                tankstelle_B=tankstelle_B,
                                tankstelle_C=tankstelle_C,
                                uhrzeit=uhrzeit,
                                verkehr=verkehr*kunde.quote,
                                app_nutzer_anteil=app_nutzer_anteil,
                                abstand_AC=abstand_AC,
                                abstand_BC=abstand_BC,
                                abstand_AB=abstand_AB,
                                fluss_A=fluss_A,
                                fluss_B=fluss_B,
                                fluss_C=fluss_C,
                                verbose=verbose
                                )
        for i in range(3):
            gesamt[i] += profit[i]  # Gewichtung nach Anzahl der Kunden
    return gesamt

def preis_zu_profit_tabelle(kunden:list, tankstelle_A, tankstelle_B, tankstelle_C, preis_start=config.preis_start, preis_end=config.preis_end, verbose=False):
    # for Tankstelle A
    tabelle_A = [0]*preis_end
    preis_origin = tankstelle_A.preis_verkauf
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_A.preis_verkauf = preis_sim
        tabelle_A[preis_sim] = gesamt_profit_volumen(kunden=kunden,
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             verbose=verbose
                             )[0]
         
    tankstelle_A.preis_verkauf = preis_origin

    # for Tankstelle B
    tabelle_B = [0]*preis_end
    preis_origin = tankstelle_B.preis_verkauf
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_B.preis_verkauf = preis_sim
        tabelle_B[preis_sim] = gesamt_profit_volumen(kunden=kunden,
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             verbose=verbose
                             )[1]
         
    tankstelle_B.preis_verkauf = preis_origin

    # for Tankstelle C
    tabelle_C = [0]*preis_end
    preis_origin = tankstelle_C.preis_verkauf
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_C.preis_verkauf = preis_sim
        tabelle_C[preis_sim] = gesamt_profit_volumen(kunden=kunden,
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             verbose=verbose
                             )[2]
         
    tankstelle_C.preis_verkauf = preis_origin

    if verbose == True:
        print("Tankstelle[A] : Preis[Cent/L] : Profit[EUR/h] ")
        for i in range(0, len(tabelle_A), 1):
            print("Tankstelle A: ", i, tabelle_A[i])

        print("Tankstelle[B] : Preis[Cent/L] : Profit[EUR/h] ")
        for i in range(0, len(tabelle_B), 1):
            print("Tankstelle B: ", i, tabelle_B[i])

        print("Tankstelle[C] : Preis[Cent/L] : Profit[EUR/h] ")
        for i in range(0, len(tabelle_C), 1):
            print("Tankstelle C: ", i, tabelle_C[i])

    return tabelle_A, tabelle_B, tabelle_C

def optimal_konstellation(wiederholungen, kunden, tankstelle_A, tankstelle_B, tankstelle_C, verbose=config.verbose_value):
    if verbose == True:
        print("=== KONSTELLATION FINDEN ===")
        print("Startpreis: Verkaufspreis Tankstelle A: ", config.preis_start_A)
        print("Startpreis: Verkaufspreis Tankstelle B: ", config.preis_start_B)
        print("Startpreis: Verkaufspreis Tankstelle C: ", config.preis_start_C)
        print("")
    for i in range(1, wiederholungen+1, 1):
        # Tankstelle A optimiert
        tabelle_A = preis_zu_profit_tabelle(kunden=kunden,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=False)[0]
        tankstelle_A.preis_verkauf = tabelle_A.index(max(tabelle_A))

        # Tankstelle B optimiert
        tabelle_B = preis_zu_profit_tabelle(kunden=kunden,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=False)[1]
        tankstelle_B.preis_verkauf = tabelle_B.index(max(tabelle_B))

        # Tankstelle C optimiert
        tabelle_C = preis_zu_profit_tabelle(kunden=kunden,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=False)[2]
        tankstelle_C.preis_verkauf = tabelle_C.index(max(tabelle_C))
        if verbose == True:
            print("=== DURCHLAUF : ", i, "===")
            print("Verkaufspreis Tankstelle A: ", tabelle_A.index(max(tabelle_A)))
            print("Verkaufspreis Tankstelle B: ", tabelle_B.index(max(tabelle_B)))
            print("Verkaufspreis Tankstelle C: ", tabelle_C.index(max(tabelle_C)))