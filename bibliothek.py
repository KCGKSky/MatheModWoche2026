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

    def aktivierung(self, X, stress):
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
        b = 1.046 * self.wendepunkt * stress
        anteil = (1 + (X/b) ** -a) ** -p
        return anteil

    def ersparnis_pro_weg(self, Tankstelle_Start, Tankstelle_Ziel, abstand:int = 1):
        return 0.01 * ( self.tankvolumen * (Tankstelle_Start.preis_verkauf - Tankstelle_Ziel.preis_verkauf) ) / ( abstand / self.fahrer_geschwindigkeit ) # EUR/h
    
    def stress_funktion(self, uhrzeit:int=config.uhrzeit):
        return 1 + ( - 0.004569 * np.cos(np.pi*uhrzeit/12) + 0.227296 * np.sin(np.pi*uhrzeit/12) - 0.083494 * np.cos(np.pi*uhrzeit/6) + 0.163494 * np.sin(np.pi*uhrzeit/6) + 0.023972 * np.cos(np.pi*uhrzeit/4) - 0.476762 * np.sin(np.pi*uhrzeit/4)) / 1.2


class Tankstelle:
    def __init__(self, preis_verkauf:int, preis_einkauf:float, energie_steuer:int = config.energie_steuer, co_2_abgabe:float = config.co_2_abgabe, mehrwert_steuer:float=config.mehrwert_steuer):
        self.preis_verkauf = preis_verkauf # EUR/L
        self.preis_einkauf = preis_einkauf # cents
        self.energie_steuer = energie_steuer # cents
        self.co_2_abgabe = co_2_abgabe # cents
        self.mehrwert_steuer = mehrwert_steuer # anteil

    # Funktion mit Margin, Einkaufspreis, Anteil an Kunden vom Pool
    def gewinn_erwartung(self, kunde:Kunde, kundschaft, uhrzeit):
        # Kundschaft ist der Anteil der Kunden den die Tankstelle bekommt
        margin = (self.preis_verkauf - self.preis_einkauf)/(1+self.mehrwert_steuer) - self.co_2_abgabe - self.energie_steuer # cent pro Liter Gewinn
        return 0.01 * kunde.tankvolumen * verkehrs_vorkommen(uhrzeit) * margin * kundschaft * config.verkehr


def verkehrs_vorkommen(uhrzeit):
    # Tabelle mit Vorkommen over Stunde
    verkehr_anteil = [0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.03, 0.09, 0.10, 0.09, 0.09, 0.07, 0.07, 0.02, 0.02, 0.03, 0.03, 0.07, 0.07, 0.08, 0.02, 0.02, 0.02, 0.01] 
    return verkehr_anteil[uhrzeit-1] 



def profit_volumen(kunde:Kunde, tankstelle_A, tankstelle_B, tankstelle_C,
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

    aktivierung_AB = kunde.aktivierung(X=ersparnis_AB, stress=kunde.stress_funktion(uhrzeit))
    aktivierung_BA = kunde.aktivierung(X=ersparnis_BA, stress=kunde.stress_funktion(uhrzeit))
    aktivierung_BC = kunde.aktivierung(X=ersparnis_BC, stress=kunde.stress_funktion(uhrzeit))
    aktivierung_AC = kunde.aktivierung(X=ersparnis_AC, stress=kunde.stress_funktion(uhrzeit))
    aktivierung_CA = kunde.aktivierung(X=ersparnis_CA, stress=kunde.stress_funktion(uhrzeit))
    aktivierung_CB = kunde.aktivierung(X=ersparnis_CB, stress=kunde.stress_funktion(uhrzeit))

    # Berechnung der Wechselwahrscheinlichkeiten, avoids total values over 
    if ersparnis_AB > ersparnis_AC:
        wechsel_A_nach_B = aktivierung_AB * fluss_A
        wechsel_A_nach_C = 0
        if tankstelle_C.preis_verkauf < tankstelle_B.preis_verkauf:
            ersparnis_A_BC = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_B, Tankstelle_Ziel=tankstelle_C,
                                                     abstand=abstand_AC - abstand_AB)
            aktivierung_A_BC = kunde.aktivierung(X=ersparnis_A_BC, stress=kunde.stress_funktion(uhrzeit))
            wechsel_BC = aktivierung_A_BC * fluss_A * app_nutzer_anteil
            wechsel_A_nach_B -= wechsel_BC
            wechsel_A_nach_C += wechsel_BC
    elif ersparnis_AB < ersparnis_AC:
        wechsel_A_nach_B = aktivierung_AB * fluss_A * (1 - app_nutzer_anteil)
        wechsel_A_nach_C = aktivierung_AC * fluss_A * app_nutzer_anteil
        if tankstelle_B.preis_verkauf < tankstelle_C.preis_verkauf:
            ersparnis_A_CB = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_C, Tankstelle_Ziel=tankstelle_B,
                                                     abstand=abstand_AB - abstand_AC)
            aktivierung_A_CB = kunde.aktivierung(X=ersparnis_A_CB, stress=kunde.stress_funktion(uhrzeit))
            wechsel_CB = aktivierung_A_CB * fluss_A * app_nutzer_anteil
            wechsel_A_nach_C -= wechsel_CB
            wechsel_A_nach_B += wechsel_CB
    else:
        wechsel_A_nach_B = 0.5 * aktivierung_AB * fluss_A * app_nutzer_anteil + aktivierung_AB * fluss_A * (1 - app_nutzer_anteil)
        wechsel_A_nach_C = 0.5 * aktivierung_AC * fluss_A * app_nutzer_anteil

    if ersparnis_BA > ersparnis_BC:
        wechsel_B_nach_A = aktivierung_BA * fluss_B
        wechsel_B_nach_C = 0
        if tankstelle_C.preis_verkauf < tankstelle_A.preis_verkauf:
            ersparnis_B_AC = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_A, Tankstelle_Ziel=tankstelle_C,
                                                     abstand=abstand_BC - abstand_AB)
            aktivierung_B_AC = kunde.aktivierung(X=ersparnis_B_AC, stress=kunde.stress_funktion(uhrzeit))
            wechsel_AC = aktivierung_B_AC * fluss_B * app_nutzer_anteil
            wechsel_B_nach_A -= wechsel_AC
            wechsel_B_nach_C += wechsel_AC
    elif ersparnis_BA < ersparnis_BC:
        wechsel_B_nach_A = aktivierung_BA * fluss_B * (1 - app_nutzer_anteil)
        wechsel_B_nach_C = aktivierung_BC * fluss_B * app_nutzer_anteil
        if tankstelle_A.preis_verkauf < tankstelle_C.preis_verkauf:
            ersparnis_B_CA = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_C, Tankstelle_Ziel=tankstelle_A,
                                                     abstand=abstand_AB - abstand_BC)
            aktivierung_B_CA = kunde.aktivierung(X=ersparnis_B_CA, stress=kunde.stress_funktion(uhrzeit))
            wechsel_CA = aktivierung_B_CA * fluss_B * app_nutzer_anteil
            wechsel_B_nach_C -= wechsel_CA
            wechsel_B_nach_A += wechsel_CA
    else:
        wechsel_B_nach_A = 0.5 * aktivierung_BA * fluss_B * app_nutzer_anteil + aktivierung_BA * fluss_B * (1 - app_nutzer_anteil)
        wechsel_B_nach_C = 0.5 * aktivierung_BC * fluss_B * app_nutzer_anteil

    if ersparnis_CA > ersparnis_CB:
        wechsel_C_nach_A = aktivierung_CA * fluss_C
        wechsel_C_nach_B = 0
        if tankstelle_B.preis_verkauf < tankstelle_A.preis_verkauf:
            ersparnis_C_AB = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_A, Tankstelle_Ziel=tankstelle_B,
                                                     abstand=abstand_BC - abstand_AC)
            aktivierung_C_AB = kunde.aktivierung(X=ersparnis_C_AB, stress=kunde.stress_funktion(uhrzeit))
            wechsel_AB = aktivierung_C_AB * fluss_C
            wechsel_C_nach_A -= wechsel_AB
            wechsel_C_nach_B += wechsel_AB
    elif ersparnis_CA < ersparnis_CB:
        wechsel_C_nach_A = 0
        wechsel_C_nach_B = aktivierung_CB * fluss_C
        if tankstelle_A.preis_verkauf < tankstelle_B.preis_verkauf:
            ersparnis_C_BA = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_B, Tankstelle_Ziel=tankstelle_A,
                                                     abstand=abstand_AC - abstand_BC)
            aktivierung_C_BA = kunde.aktivierung(X=ersparnis_C_BA, stress=kunde.stress_funktion(uhrzeit))
            wechsel_BA = aktivierung_C_BA * fluss_C
            wechsel_C_nach_B -= wechsel_BA
            wechsel_C_nach_A += wechsel_BA
    else:
        wechsel_C_nach_A = 0.5 * aktivierung_CA * fluss_C
        wechsel_C_nach_B = 0.5 * aktivierung_CB * fluss_C

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
    profit_volumen_A = tankstelle_A.gewinn_erwartung(kunde = kunde, kundschaft=kundschaft_A, uhrzeit=uhrzeit)
    profit_volumen_B = tankstelle_B.gewinn_erwartung(kunde = kunde, kundschaft=kundschaft_B, uhrzeit=uhrzeit)
    profit_volumen_C = tankstelle_C.gewinn_erwartung(kunde = kunde, kundschaft=kundschaft_C, uhrzeit=uhrzeit)

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

        print("Verkaufspreis Tankstelle A: ", tankstelle_A.preis_verkauf, "[Cent/L]")
        print("Verkaufspreis Tankstelle B: ", tankstelle_B.preis_verkauf, "[Cent/L]")
        print("Verkaufspreis Tankstelle C: ", tankstelle_C.preis_verkauf, "[Cent/L]")

        print("======")

        print("Einkaufspreis Tankstelle A: ", tankstelle_A.preis_einkauf, "[Cent/L]")
        print("Einkaufspreis Tankstelle B: ", tankstelle_B.preis_einkauf, "[Cent/L]")
        print("Einkaufspreis Tankstelle C: ", tankstelle_C.preis_einkauf, "[Cent/L]")

        print("=======")

        print("Uhrzeit: ", uhrzeit)
        print("App Nutzer Anteil: ", app_nutzer_anteil)
        print("Tankvorgange: ", verkehr)
        print("Tankvolumen: ", kunde.tankvolumen)

        print("=======")

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

def preis_zu_profit_tabelle(kunden:list, tankstelle_A, tankstelle_B, tankstelle_C, preis_start=config.preis_start, preis_end=config.preis_end, verbose=False, uhrzeit:int = config.uhrzeit):
    # for Tankstelle A
    tabelle_A = [0]*preis_end
    preis_origin = tankstelle_A.preis_verkauf
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_A.preis_verkauf = preis_sim
        tabelle_A[preis_sim] = gesamt_profit_volumen(kunden=kunden,
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             verbose=verbose,
                             uhrzeit=uhrzeit
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
                             uhrzeit=uhrzeit,
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
                             uhrzeit=uhrzeit,
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

def optimal_konstellation(kunden:list, tankstelle_A, tankstelle_B, tankstelle_C, verbose=config.verbose_value, simultan:bool = False, uhrzeit_start:int = config.uhrzeit, uhrzeit_end:int = config.uhrzeit, verlauf :bool = False):
    """
    Berechnet so lange die optimalen Verkaufspreise für die Tankstellen, bis sich eine Konstellation wiederholt. Gibt die Konstellation zurück, die sich wiederholt.
    """
    if verbose == True:
        print("=== KONSTELLATION FINDEN ===")
        print("Startpreis: Verkaufspreis Tankstelle A: ", config.preis_start_A)
        print("Startpreis: Verkaufspreis Tankstelle B: ", config.preis_start_B)
        print("Startpreis: Verkaufspreis Tankstelle C: ", config.preis_start_C)
        print("")

    konstellationen = [[
        0,
        tankstelle_A.preis_verkauf,
        tankstelle_B.preis_verkauf,
        tankstelle_C.preis_verkauf,
    ]]
    durchlauf = 0

    while True:
         durchlauf += 1
         if simultan:
             tabelle = np.array([0] * config.preis_end)
             tabelle = np.array([tabelle, tabelle.copy(), tabelle.copy()])
             for i in range(uhrzeit_start, uhrzeit_end + 1, 1):
                 result = preis_zu_profit_tabelle(kunden=kunden,
                                       tankstelle_A=tankstelle_A,
                                       tankstelle_B=tankstelle_B,
                                       tankstelle_C=tankstelle_C,
                                       verbose=False,
                                       uhrzeit=i)
                 tabelle[0] = np.array(tabelle[0]) + np.array(result[0])
                 tabelle[1] = np.array(tabelle[1]) + np.array(result[1])
                 tabelle[2] = np.array(tabelle[2]) + np.array(result[2])
             tabelle_A = tabelle[0]
             tabelle_B = tabelle[1]
             tabelle_C = tabelle[2]
         else:
             # Tankstelle A optimiert - für alle Uhrzeiten von uhrzeit_start bis uhrzeit_end
             tabelle_A = np.array([0] * config.preis_end)
             tabelle_B = np.array([0] * config.preis_end)
             tabelle_C = np.array([0] * config.preis_end)
             for i in range(uhrzeit_start, uhrzeit_end+1, 1):
                 for j in range(3):
                     result = preis_zu_profit_tabelle(kunden=kunden,
                                           tankstelle_A=tankstelle_A,
                                           tankstelle_B=tankstelle_B,
                                           tankstelle_C=tankstelle_C,
                                           verbose=False,
                                           uhrzeit=i)[j]
                     if j == 0:
                         tabelle_A = np.array(tabelle_A) + np.array(result)
                     elif j == 1:
                         tabelle_B = np.array(tabelle_B) + np.array(result)
                     else:
                         tabelle_C = np.array(tabelle_C) + np.array(result)

         tankstelle_A.preis_verkauf = int(np.argmax(tabelle_A))
         tankstelle_B.preis_verkauf = int(np.argmax(tabelle_B))
         tankstelle_C.preis_verkauf = int(np.argmax(tabelle_C))

         aktuelle_preise = [
             tankstelle_A.preis_verkauf,
             tankstelle_B.preis_verkauf,
             tankstelle_C.preis_verkauf,
         ]
         aktuelle_konstellation = [durchlauf, *aktuelle_preise]
         konstellationen.append(aktuelle_konstellation)

         if verbose == True:
             print("=== DURCHLAUF : ", durchlauf, "===")
             print("Verkaufspreis Tankstelle A: ", int(np.argmax(tabelle_A)))
             print("Verkaufspreis Tankstelle B: ", int(np.argmax(tabelle_B)))
             print("Verkaufspreis Tankstelle C: ", int(np.argmax(tabelle_C)))
             print("Aktuelle Konstellation: ", aktuelle_konstellation)

         start = next(
             (
                 index
                 for index, konstellation in enumerate(konstellationen[:-1])
                 if konstellation[1:] == aktuelle_preise
             ),
             None,
         )
         if start is not None:
             print(verlauf)
             if verlauf == True:
                 return konstellationen
             loop = konstellationen[start:]
             if len(loop) == 2:
                 if verbose == True : print("=== STABILER ZUSTAND ERREICHT ===")
                 if verbose == True : print("Konstellation ",
                       loop[0][0],
                       ": A = ",
                       loop[0][1],
                       " B = ",
                       loop[0][2],
                       " C = ",
                       loop[0][3])
                 return loop[0][1:]  # remove the Durchlauf number and return only the prices
             else:
                  if verbose == True : print("=== LOOP ERREICHT ===")
                  if verbose == True:
                      for konstellation in loop:
                          print(
                              "Konstellation ",
                              konstellation[0],
                              ": A = ",
                              konstellation[1],
                              " B = ",
                              konstellation[2],
                              " C = ",
                              konstellation[3],
                          )
                  preisbereiche = []
                  for tankstelle in range(1, 4):
                      werte = [konstellation[tankstelle] for konstellation in loop]
                      preisbereiche.append(min(werte))
                      preisbereiche.append(max(werte))
                  if verbose == True :
                      print("=== PREISRANGE IM LOOP ===")
                      print("Tankstelle A: ", preisbereiche[0], "-", preisbereiche[1])
                      print("Tankstelle B: ", preisbereiche[2], "-", preisbereiche[3])
                      print("Tankstelle C: ", preisbereiche[4], "-", preisbereiche[5])
                      print("Loop-Länge: ", len(loop)-1)
                      print("Loop gefunden nach ", len(konstellationen), " Durchläufen")

                  # Berechne Durchschnitt der Konstellationen im Loop
                  durchschnitt_A = np.mean([konstellation[1] for konstellation in loop])
                  durchschnitt_B = np.mean([konstellation[2] for konstellation in loop])
                  durchschnitt_C = np.mean([konstellation[3] for konstellation in loop])
                  durchschnitt_konstellation = [int(round(durchschnitt_A)), int(round(durchschnitt_B)), int(round(durchschnitt_C))]

                  if verbose == True:
                      print("=== DURCHSCHNITTSKONSTELLATION IM LOOP ===")
                      print("A = ", durchschnitt_konstellation[0])
                      print("B = ", durchschnitt_konstellation[1])
                      print("C = ", durchschnitt_konstellation[2])
                      print(durchschnitt_konstellation)

                  return durchschnitt_konstellation
