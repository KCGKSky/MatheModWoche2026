import numpy as np
import matplotlib.pyplot as plt
import bibliothek as bib
import draw_utils as dr
from matplotlib.widgets import Button, Slider



# Initialisierung Kunden
kunde = bib.Kunde(1000)
vollzeit_kunde = bib.Kunde(40, tankvolumen=60) # Wendepunkt (theoretischer Wert) EURO die Stunde
teilzeit_kunde = bib.Kunde(20)
unbeschaftigt_kunde = bib.Kunde(10)

# Initialisierung Tankstellen
tankstelle_A = bib.Tankstelle(200) # Preis
tankstelle_B = bib.Tankstelle(210)
tankstelle_C = bib.Tankstelle(199)

uhrzeit = 15

abstand_AB = 0.1
abstand_BC = 2.1
abstand_AC = 2.0

fluss_A = 0.5
fluss_B = 0.5
fluss_C = 0

ersparnis_AB = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_A, Tankstelle_Ziel=tankstelle_B, abstand=abstand_AB)
ersparnis_BA = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_B, Tankstelle_Ziel=tankstelle_A, abstand=abstand_AB)
ersparnis_AC = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_A, Tankstelle_Ziel=tankstelle_C, abstand=abstand_AC)
ersparnis_BC = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_B, Tankstelle_Ziel=tankstelle_C, abstand=abstand_BC)
ersparnis_CA = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_C, Tankstelle_Ziel=tankstelle_A, abstand=abstand_AC)
ersparnis_CB = kunde.ersparnis_pro_weg(Tankstelle_Start=tankstelle_C, Tankstelle_Ziel=tankstelle_B, abstand=abstand_BC)


aktivierung_AB = kunde.aktivierung(X=ersparnis_AB, uhrzeit=uhrzeit)
aktivierung_BA = kunde.aktivierung(X=ersparnis_BA, uhrzeit=uhrzeit)
aktivierung_BC = kunde.aktivierung(X=ersparnis_BC, uhrzeit=uhrzeit)
aktivierung_AC = kunde.aktivierung(X=ersparnis_AC, uhrzeit=uhrzeit)
aktivierung_CA = kunde.aktivierung(X=ersparnis_CA, uhrzeit=uhrzeit)
aktivierung_CB = kunde.aktivierung(X=ersparnis_CB, uhrzeit=uhrzeit)


kundschaft_A = fluss_A - aktivierung_AB * fluss_A + aktivierung_BA * fluss_B + aktivierung_CA * fluss_C
kundschaft_B = fluss_A - aktivierung_BA * fluss_B + aktivierung_AB * fluss_A + aktivierung_CB * fluss_C
kundschaft_C = fluss_C - aktivierung_AC * fluss_C + aktivierung_BC * fluss_B + aktivierung_AC * fluss_A

profit_volumen_A = tankstelle_A.profit_volumen(kundschaft=kundschaft_A)
profit_volumen_B = tankstelle_B.profit_volumen(kundschaft=kundschaft_B)
profit_volumen_C = tankstelle_C.profit_volumen(kundschaft=kundschaft_C)

print("")

print("=== INFORMATION TANKSTELLE VERGLEICH A & B ===")

print("===")

print("Fluss A", fluss_A)
print("Fluss B", fluss_B)
print("Fluss C", fluss_C)

print("===")

print("Preis Tankstelle A: ", tankstelle_A.verkaufs_preis, "Cent")
print("Preis Tankstelle B: ", tankstelle_B.verkaufs_preis, "Cent")
print("Preis Tankstelle C: ", tankstelle_C.verkaufs_preis, "Cent")

print("=======")

print("Uhrzeit: ", uhrzeit)

print("=======")

print("Ersparnis von A nach B: ", ersparnis_AB, "EUR/h")
print("Ersparnis von A nach C: ", ersparnis_AC, "EUR/h")
print("Ersparnis von B nach A: ", ersparnis_BA, "EUR/h")
print("Ersparnis von B nach C: ", ersparnis_BC, "EUR/h")
print("Ersparnis von C nach A: ", ersparnis_CA, "EUR/h")
print("Ersparnis von C nach B: ", ersparnis_CB, "EUR/h")

print("=======")

print("Kundschaft Gesamt: ", kundschaft_A + kundschaft_B + kundschaft_C)
print("Kundschaft der Tankstelle A: ", kundschaft_A)
print("Kundschaft der Tankstelle B: ", kundschaft_B)
print("Kundschaft der Tankstelle C: ", kundschaft_C)

print("=======")

print("Profit Volumen Tankstelle A", profit_volumen_A) 
print("Profit Volumen Tankstelle B", profit_volumen_B)
print("Profit Volumen Tankstelle C", profit_volumen_C)

