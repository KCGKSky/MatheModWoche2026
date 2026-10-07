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

kunden = [
    bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, tankvolumen=config.tankvolumen, quote= 1),
    bib.Kunde(wendepunkt=config.wendepunkt_teilzeit, tankvolumen=config.tankvolumen, quote= 0),
    bib.Kunde(wendepunkt=config.wendepunkt_unbeschaftigt, tankvolumen=config.tankvolumen, quote= 0)
]

preis_end = config.preis_end


    



tabelle = bib.preis_zu_profit_tabelle(kunden=kunden,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  preis_end=preis_end,

                                  verbose=True)


print("Optimalpreis fur Tankstelle A:", tabelle[0].index(max(tabelle[0])))
print("Optimalpreis fur Tankstelle B:", tabelle[1].index(max(tabelle[1])))
print("Optimalpreis fur Tankstelle C:", tabelle[2].index(max(tabelle[2])))



bib.gesamt_profit_volumen(kunden=kunden,
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
                             )