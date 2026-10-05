import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib

# Set x linear space
x = np.linspace(0, 5, 100)

# Parameters
delta_tankpreis = 1 #cents
distanz = 0.3 # kilometer
fahrer_geschwindigkeit = 60 #km/h
tankvolumen = 60 # Liter

vollzeit_kunde = bib.Kunde(3)
teilzeit_kunde = bib.Kunde(3)
unbeschaftigt_kunde = bib.Kunde(1)





figure, ax = plt.subplots()




ax.plot(x, bib.aktivierung(x, 2), "m")


plt.title("Aktivierung der Kunden zum Wechseln")
plt.xlabel("Ersparnis pro Stunde Weg")
plt.ylabel("Anteil der Wechsler")
plt.show()






