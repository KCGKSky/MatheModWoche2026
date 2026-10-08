import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import config as config
import draw_utils as dr
# from matplotlib.widgets import Slider

verbose_value = config.verbose_value

tankstelle_A = bib.Tankstelle(preis_verkauf=config.preis_start_A,
                              preis_einkauf=config.preis_einkauf_A,
                              co_2_abgabe=config.co_2_abgabe,
                              energie_steuer=config.energie_steuer,
                              mehrwert_steuer=config.mehrwert_steuer
                              )
tankstelle_B = bib.Tankstelle(preis_verkauf=config.preis_start_B,
                              preis_einkauf=config.preis_einkauf_B,
                              co_2_abgabe=config.co_2_abgabe,
                              energie_steuer=config.energie_steuer,
                              mehrwert_steuer=config.mehrwert_steuer
                              )
tankstelle_C = bib.Tankstelle(preis_verkauf=config.preis_start_C,
                              preis_einkauf=config.preis_einkauf_C,
                              co_2_abgabe=config.co_2_abgabe,
                              energie_steuer=config.energie_steuer,
                              mehrwert_steuer=config.mehrwert_steuer
                              )

kunden = [
    bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, quote=config.quote_vollzeit),
    bib.Kunde(wendepunkt=config.wendepunkt_teilzeit, quote=config.quote_teilzeit),
    bib.Kunde(wendepunkt=config.wendepunkt_unbeschaftigt, quote=config.quote_unbeschaftigt)
]

### PRESENTATION START
print("=== PROGRAMM START ===")
dr.plot_einkommensverteilung(5, 200000)
dr.plot_aktivierung(6, kunden, 250)
plt.show(block=False)
input("WEITER Mit Stress_funktion? : ")

dr.plot_stress_function(0, kunden)
dr.plot_verkehrs_vorkommen(7)
plt.show(block=False)
input("WEITER Information Darstellung? : ")

## PRINT INFORMATION
bib.profit_volumen(kunde=kunden[0], tankstelle_A=tankstelle_A, tankstelle_B=tankstelle_B, tankstelle_C=tankstelle_C, verbose=True)
#Preisempfehlung herausfinden
a, b, c = bib.preis_zu_profit_tabelle(kunden, tankstelle_A, tankstelle_B, tankstelle_C)
print("Tankstelle Benzinpreisempfehlung: ", a.index(max(a)))
print("Tankstelle Benzinpreisempfehlung: ", b.index(max(b)))
print("Tankstelle Benzinpreisempfehlung: ", c.index(max(c)))

input("WEITER Mit Verlauf der Benzinpreiseinpendelung? : ")

# Optimierung nachvollziehbar zeigen
a, b, c = bib.optimal_konstellation(kunden, tankstelle_A, tankstelle_B, tankstelle_C, verbose=True)
print("=== Eingependelte Benzinpreise ===")
print("Tankstelle A: ", a)
print("Tankstelle B: ", b)
print("Tankstelle C: ", c)
dr.plot_konstellations_verlauf(4, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 25-config.zeit_fenster, 24, False)
plt.show(block=False)

input("WEITER mit Graphiken (dauert circa 30 Sekunden)?: ")

dr.plot_profit_over_uhrzeit_fest(1, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 0, 24, False)
dr.plot_preis_zu_profit(4, kunden, tankstelle_A, tankstelle_B, tankstelle_C, config.uhrzeit, False)
dr.plot_profit_over_uhrzeit_optimized(2, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 0, 24, False)
dr.plot_preis_over_uhrzeit_optimized(3, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 0, 24, False)
bib.profit_volumen(kunde=kunden[0], tankstelle_A=tankstelle_A, tankstelle_B=tankstelle_B, tankstelle_C=tankstelle_C, verbose=True)
plt.show(block=False)

while(True):
    answer = input("WEITER: END PROGRAMM (type 'yes')? :")
    if answer == "YES" or answer == "yes" : break     

print("=== PROGRAMM ENDE ===")