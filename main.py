import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib

# Set x linear space
x = np.linspace(0, 5, 100)

# Initialisierung Kunden
vollzeit_kunde = bib.Kunde(3) # Wendepunkt (theoretischer Wert)
teilzeit_kunde = bib.Kunde(3)
unbeschaftigt_kunde = bib.Kunde(1)

# Initialisierung Tankstellen
tankstelle_A = bib.Tankstelle(200, 0) # Preis, Entfernung km
tankstelle_B = bib.Tankstelle(200, 0.2)
tankstelle_C = bib.Tankstelle(190, 2)



"""
figure, ax = plt.subplots()

ax.plot(x, bib.aktivierung(x, 2), "m")


plt.title("Aktivierung der Kunden zum Wechseln")
plt.xlabel("Ersparnis pro Stunde Weg")
plt.ylabel("Anteil der Wechsler")
plt.show()
"""





