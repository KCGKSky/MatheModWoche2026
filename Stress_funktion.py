import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

# Mittelpunkte der Zeitintervalle
x = np.array([3, 7.5, 10.5, 14, 17.5, 21.5])

# Ursprüngliche Werte
y_alt = np.array([3, 1, 16/7, 2, 39/14, 1])

# Lineare Abbildung auf die neue Skala:
# 1 -> 1, 2 -> 1.5, 3 -> 2
y = 0.5 * y_alt + 0.5

# Glatte Kurve durch die Punkte
f = PchipInterpolator(x, y)

# Viele x-Werte für glatte Darstellung
x_smooth = np.linspace(3, 21.5, 1000)
y_smooth = f(x_smooth)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(x_smooth, y_smooth, linewidth=2, label="Graph")
plt.scatter(x, y, zorder=3)

# Achsen
plt.xlim(0, 24)
plt.ylim(0, 2)

# Beschriftung
plt.xlabel("Uhrzeit")
plt.ylabel("Wert")

plt.xticks(
    [3, 7.5, 10.5, 14, 17.5, 21.5],
    ["0–6", "6–9", "9–12", "12–16", "16–19", "19–24"]
)

plt.yticks(np.arange(0, 2.1, 0.25))

plt.title("Graph der transformierten Werte")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()