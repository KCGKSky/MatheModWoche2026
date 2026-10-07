import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import config
# from matplotlib.widgets import Slider

verbose_value = config.verbose_value

tankstelle_A = bib.Tankstelle(preis_verkauf=config.preis_start_A,
                              preis_einkauf=config.preis_einkauf_A,
                              co_2_abgabe=config.co_2_abgabe,
                              energie_steuer=config.energie_steuer,
                              mehrwert_steuer=config.mehrwert_steuer,
                              )
tankstelle_B = bib.Tankstelle(preis_verkauf=config.preis_start_B,
                              preis_einkauf=config.preis_einkauf_B,
                              co_2_abgabe=config.co_2_abgabe,
                              energie_steuer=config.energie_steuer,
                              mehrwert_steuer=config.mehrwert_steuer,
                              )
tankstelle_C = bib.Tankstelle(preis_verkauf=config.preis_start_C,
                              preis_einkauf=config.preis_einkauf_C,
                              co_2_abgabe=config.co_2_abgabe,
                              energie_steuer=config.energie_steuer,
                              mehrwert_steuer=config.mehrwert_steuer,
                              )

kunde_0 = bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, tankvolumen=config.tankvolumen)
kunde_1 = bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, tankvolumen=config.tankvolumen)
kunde_2 = bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, tankvolumen=config.tankvolumen)

tabelle = bib.preis_zu_profit_tabelle(kunde=kunde_0,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C, 
                                  verbose=False)


print("Optimalpreis fur Tankstelle A:", tabelle[0].index(max(tabelle[0])))
print("Optimalpreis fur Tankstelle B:", tabelle[1].index(max(tabelle[1])))
print("Optimalpreis fur Tankstelle C:", tabelle[2].index(max(tabelle[2])))



bib.profit_volumen(kunde=kunde_0, 
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=False
                    )

def optimal_konstellation(wiederholungen, verbose=config.verbose_value):
    if verbose == True:
        print("=== KONSTELLATION FINDEN ===")
        print("Startpreis: Verkaufspreis Tankstelle A: ", config.preis_start_A)
        print("Startpreis: Verkaufspreis Tankstelle B: ", config.preis_start_B)  
        print("Startpreis: Verkaufspreis Tankstelle C: ", config.preis_start_C)
        print("")
    for i in range(1, wiederholungen+1, 1):
        # Tankstelle A optimiert
        tabelle_A = bib.preis_zu_profit_tabelle(kunde=kunde_0,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=False)[0]
        tankstelle_A.preis_verkauf = tabelle_A.index(max(tabelle_A))

        # Tankstelle B optimiert
        tabelle_B = bib.preis_zu_profit_tabelle(kunde=kunde_0,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C, 
                                  verbose=False)[1]
        tankstelle_B.preis_verkauf = tabelle_B.index(max(tabelle_B))

        # Tankstelle C optimiert
        tabelle_C = bib.preis_zu_profit_tabelle(kunde=kunde_0,
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

optimal_konstellation(20)