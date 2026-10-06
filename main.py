import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import draw_utils as dr


# Initialisierung Kunden
vollzeit_kunde = bib.Kunde(40, tankvolumen=60) # Wendepunkt (theoretischer Wert) EURO die Stunde
teilzeit_kunde = bib.Kunde(20)
unbeschaftigt_kunde = bib.Kunde(10)

# Initialisierung Tankstellen
tankstelle_A = bib.Tankstelle(200, 0) # Preis, Entfernung km
tankstelle_B = bib.Tankstelle(199, 0.5)
tankstelle_C = bib.Tankstelle(199, 2)

print("Anteil der Wechsler, Vollzeitkunde, ", vollzeit_kunde.ersparnis_pro_weg(tankstelle_A, tankstelle_B) ,vollzeit_kunde.aktivierung(vollzeit_kunde.ersparnis_pro_weg(tankstelle_A, tankstelle_B)))

#dr.draw_plot(unbeschaftigt_kunde.aktivierung, "Aktivierungsfunktion unbeschaftigt")
dr.draw_plot(vollzeit_kunde.aktivierung, "Aktivierungsfunktion vollzeit")
plt.show()












