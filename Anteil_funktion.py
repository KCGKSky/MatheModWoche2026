import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

# Mittelpunkte der Zeitintervalle
x = np.array([3, 7.5, 10.5, 14, 17.5, 21.5])

# Zeile 1
y1 = np.array([
    0.40,
    8/11,
    2/7,
    0.375,
    11/14,
    4/23
])

# Zeile 2
y2 = np.array([
    0.20,
    1/11,
    1/7,
    0.125,
    3/28,
    2/23
])

# Zeile 3
y3 = np.array([
    0.40,
    2/11,
    4/7,
    0.50,
    3/28,
    17/23
])

# Glatte Kurven, die exakt durch die Werte laufen
f1 = PchipInterpolator(x, y1)
f2 = PchipInterpolator(x, y2)
f3 = PchipInterpolator(x, y3)

# Viele x-Werte für eine glatte Darstellung
x_smooth = np.linspace(3, 21.5, 1000)

# Diagramm erstellen
plt.figure(figsize=(12, 6))

plt.plot(x_smooth, f1(x_smooth), label="Zeile 1", linewidth=2)
plt.plot(x_smooth, f2(x_smooth), label="Zeile 2", linewidth=2)
plt.plot(x_smooth, f3(x_smooth), label="Zeile 3", linewidth=2)

# Originalwerte als Punkte anzeigen
plt.scatter(x, y1)
plt.scatter(x, y2)
plt.scatter(x, y3)

# Achsenbereiche
plt.xlim(0, 24)
plt.ylim(0, 1)

# Beschriftung
plt.xlabel("Uhrzeit")
plt.ylabel("Anteil")

# x-Achse mit Zeitintervallen
plt.xticks(
    [3, 7.5, 10.5, 14, 17.5, 21.5],
    ["0–6", "6–9", "9–12", "12–16", "16–19", "19–24"]
)

# y-Achse als Prozentwerte
yticks = np.arange(0, 1.1, 0.1)
plt.yticks(yticks, [f"{int(v*100)}%" for v in yticks])

plt.title("Verteilung nach Uhrzeit")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()