import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import draw_utils as dr
from matplotlib.widgets import Button, Slider



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
#dr.draw_plot(vollzeit_kunde.aktivierung, "Aktivierungsfunktion vollzeit")
#plt.show()



x = np.linspace(0, 100, 1000)
fig, ax = plt.subplots()

ax.plot(x, vollzeit_kunde.stress_funktion(x))

line, = ax.plot(x, vollzeit_kunde.aktivierung(x))
fig.subplots_adjust(left=0.25, bottom=0.25)

axfreq = fig.add_axes((0.25, 0.1, 0.65, 0.03))
uhrzeit_slider = Slider(
    ax=axfreq,
    label='Uhrzeit',
    valmin=0,
    valmax=24,
    valinit=12,
)

def update(val):
    line.set_ydata(vollzeit_kunde.aktivierung(x, uhrzeit=uhrzeit_slider.val))
    fig.canvas.draw_idle()

uhrzeit_slider.on_changed(update)

plt.show()




