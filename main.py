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

dr.plot_stress_function(0, kunden)
dr.plot_profit_over_uhrzeit_fest(1, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 0, 24, True)
dr.plot_profit_over_uhrzeit_optimized(2, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 0, 24, True)
dr.plot_preis_over_uhrzeit_optimized(3, kunden, tankstelle_A, tankstelle_B, tankstelle_C, 0, 24, True)

plt.show()


#bib.optimal_konstellation(simultan = False, kunden=kunden, tankstelle_A=tankstelle_A, tankstelle_B=tankstelle_B, tankstelle_C=tankstelle_C, verbose=False)