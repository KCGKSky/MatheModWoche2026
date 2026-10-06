import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import config
# from matplotlib.widgets import Slider

verbose_value = config.verbose_value

tankstelle_A = bib.Tankstelle(config.preis_start_A)
tankstelle_B = bib.Tankstelle(config.preis_start_B)
tankstelle_C = bib.Tankstelle(config.preis_start_C)

uhrzeit = config.uhrzeit
app_nutzer_anteil = config.app_nutzer_anteil
verkehr = config.verkehr

abstand_AB = config.abstand_AB
abstand_BC = config.abstand_BC
abstand_AC = config.abstand_AC

fluss_A = config.fluss_A
fluss_B = config.fluss_B
fluss_C = config.fluss_C

kunde = bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, tankvolumen=config.tankvolumen)

# Preise in cent
preis_end = 250


def preis_zu_profit_volumen_tabelle(kunde, preis_start=0, preis_end=100, verbose=False):
    tankstelle_A = bib.Tankstelle(config.preis_start_A)
    tankstelle_B = bib.Tankstelle(config.preis_start_B)
    tankstelle_C = bib.Tankstelle(config.preis_start_C)

    reihen, spalten = (preis_end, 3)
    tabelle = [[0 for i in range(reihen)] for j in range(spalten)]

    # for Tankstelle A
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_A.preis_verkauf = preis_sim
        tabelle[0][preis_sim] = bib.profit_volumen_auswerten(kunde=kunde, 
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             uhrzeit=uhrzeit,
                             verkehr=verkehr,
                             app_nutzer_anteil=app_nutzer_anteil,
                             abstand_AC=abstand_AC,
                             abstand_BC=abstand_BC,
                             abstand_AB=abstand_AB,
                             fluss_A=fluss_A,
                             fluss_B=fluss_B,
                             fluss_C=fluss_C,
                             verbose=False
                             )[0]
         
    tankstelle_A.preis_verkauf = config.preis_start_A

    # for Tankstelle B
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_B.preis_verkauf = preis_sim
        tabelle[1][preis_sim] = bib.profit_volumen_auswerten(kunde=kunde, 
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             uhrzeit=uhrzeit,
                             verkehr=verkehr,
                             app_nutzer_anteil=app_nutzer_anteil,
                             abstand_AC=abstand_AC,
                             abstand_BC=abstand_BC,
                             abstand_AB=abstand_AB,
                             fluss_A=fluss_A,
                             fluss_B=fluss_B,
                             fluss_C=fluss_C,
                             verbose=False
                             )[1]
         
    tankstelle_B.preis_verkauf = config.preis_start_B

    # for Tankstelle C
    for preis_sim in range(preis_start, preis_end, 1):
        tankstelle_C.preis_verkauf = preis_sim
        tabelle[2][preis_sim] = bib.profit_volumen_auswerten(kunde=kunde, 
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             uhrzeit=uhrzeit,
                             verkehr=verkehr,
                             app_nutzer_anteil=app_nutzer_anteil,
                             abstand_AC=abstand_AC,
                             abstand_BC=abstand_BC,
                             abstand_AB=abstand_AB,
                             fluss_A=fluss_A,
                             fluss_B=fluss_B,
                             fluss_C=fluss_C,
                             verbose=False
                             )[2]
         
    tankstelle_C.preis_verkauf = config.preis_start_C
    if verbose == True:
        for i in range(0, len(tabelle[0]), 1):
            print("Tankstelle A: ", i, tabelle[0][i])

        for i in range(0, len(tabelle[0]), 1):
            print("Tankstelle B: ", i, tabelle[1][i])

        for i in range(0, len(tabelle[0]), 1):
            print("Tankstelle C: ", i, tabelle[2][i])

    return tabelle
    


tabelle = preis_zu_profit_volumen_tabelle(kunde=kunde, preis_end=preis_end, verbose=False)


print("Optimalpreis fur Tankstelle A:", tabelle[0].index(max(tabelle[0])))
print("Optimalpreis fur Tankstelle B:", tabelle[1].index(max(tabelle[1])))
print("Optimalpreis fur Tankstelle C:", tabelle[2].index(max(tabelle[2])))


bib.profit_volumen_auswerten(kunde=kunde, 
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             uhrzeit=uhrzeit,
                             verkehr=verkehr,
                             app_nutzer_anteil=app_nutzer_anteil,
                             abstand_AC=abstand_AC,
                             abstand_BC=abstand_BC,
                             abstand_AB=abstand_AB,
                             fluss_A=fluss_A,
                             fluss_B=fluss_B,
                             fluss_C=fluss_C,
                             verbose=True
                             )