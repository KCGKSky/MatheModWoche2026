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

kunden = [
    bib.Kunde(wendepunkt=config.wendepunkt_vollzeit, quote=config.quote_vollzeit),
    bib.Kunde(wendepunkt=config.wendepunkt_teilzeit, quote=config.quote_teilzeit),
    bib.Kunde(wendepunkt=config.wendepunkt_unbeschaftigt, quote=config.quote_unbeschaftigt)
]


bib.profit_volumen(kunde=kunden[0],
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=True
                    )

print(bib.gesamt_profit_volumen(kunden=kunden,
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=True
                    ))

tabelle = bib.preis_zu_profit_tabelle(kunden=kunden,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=False)


plt.plot(tabelle[0], label="Tankstelle A")
plt.plot(tabelle[1], label="Tankstelle B")
plt.plot(tabelle[2], label="Tankstelle C")
plt.xlabel("Preis pro Liter")
plt.ylabel("Profit EURO")
plt.legend()
plt.grid(True)
plt.show()

bib.optimal_konstellation(20, kunden=kunden, tankstelle_A=tankstelle_A, tankstelle_B=tankstelle_B, tankstelle_C=tankstelle_C, verbose=False)