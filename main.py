import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import draw_utils as dr
from matplotlib.widgets import Button, Slider

verbose_value = False

# Initialisierung Kunden
kunde = bib.Kunde(75, tankvolumen = 100)

# Initialisierung Tankstellen
tankstelle_A = bib.Tankstelle(200)
tankstelle_B = bib.Tankstelle(200)
tankstelle_C = bib.Tankstelle(190)

# Parameter
uhrzeit = 10
app_nutzer_anteil = 1.0

abstand_AB = 1
abstand_BC = 5
abstand_AC = 5

fluss_A = 0.5
fluss_B = 0.5
fluss_C = 0


volume_list = bib.profit_volumen_auswerten(kunde=kunde, 
                             tankstelle_A=tankstelle_A,
                             tankstelle_B=tankstelle_B,
                             tankstelle_C=tankstelle_C,
                             uhrzeit=uhrzeit,
                             abstand_AC=abstand_AC,
                             abstand_BC=abstand_BC,
                             abstand_AB=abstand_AB,
                             fluss_A=fluss_A,
                             fluss_B=fluss_B,
                             fluss_C=fluss_C,
                             verbose=verbose_value
                             )

print(volume_list)