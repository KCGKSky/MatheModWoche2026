import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import draw_utils as dr



# Initialisierung Kunden
vollzeit_kunde = bib.Kunde(3) # Wendepunkt (theoretischer Wert)
teilzeit_kunde = bib.Kunde(3)
unbeschaftigt_kunde = bib.Kunde(1)

# Initialisierung Tankstellen
tankstelle_A = bib.Tankstelle(200, 0) # Preis, Entfernung km
tankstelle_B = bib.Tankstelle(200, 0.2)
tankstelle_C = bib.Tankstelle(190, 2)

dr.draw_plot(unbeschaftigt_kunde.aktivierung, "Aktivierungsfunktion")






