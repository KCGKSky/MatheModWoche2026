import numpy as np
import matplotlib.pyplot as plt


def B(x):
    if 0 <= x <= 3:
        return 0.03
    elif 3 < x <= 7.5:
        return -0.004170096022 * (x - 3)**3 + 0.028148148148 * (x - 3)**2 + 0.03
    elif 7.5 < x <= 10.5:
        return 0.013333333333 * (x - 7.5)**3 - 0.06 * (x - 7.5)**2 + 0.22
    elif 10.5 < x <= 14:
        return 0.04
    elif 14 < x <= 17.5:
        return -0.005597667638 * (x - 14)**3 + 0.029387755102 * (x - 14)**2 + 0.04
    elif 17.5 < x <= 21.5:
        return 0.004375 * (x - 17.5)**3 - 0.02625 * (x - 17.5)**2 + 0.16
    elif 21.5 < x <= 24:
        return 0.02
    else:
        return np.nan


def O(x):
    if 0 <= x <= 3:
        return 0.01
    elif 3 < x <= 7.5:
        return -0.000438957476 * (x - 3)**3 + 0.002962962963 * (x - 3)**2 + 0.01
    elif 7.5 < x <= 10.5:
        return 0.000740740741 * (x - 7.5)**3 - 0.003333333333 * (x - 7.5)**2 + 0.03
    elif 10.5 < x <= 17.5:
        return 0.02
    elif 17.5 < x <= 21.5:
        return 0.0003125 * (x - 17.5)**3 - 0.001875 * (x - 17.5)**2 + 0.02
    elif 21.5 < x <= 24:
        return 0.01
    else:
        return np.nan


def G(x):
    if 0 <= x <= 3:
        return 0.04
    elif 3 < x <= 7.5:
        return 0.000219478738 * (x - 3)**3 - 0.001481481481 * (x - 3)**2 + 0.04
    elif 7.5 < x <= 10.5:
        return -0.01037037037 * (x - 7.5)**3 + 0.046666666667 * (x - 7.5)**2 + 0.03
    elif 10.5 < x <= 14:
        return 0.006064139942 * (x - 10.5)**3 - 0.031836734694 * (x - 10.5)**2 + 0.17
    elif 14 < x <= 24:
        return 0.04
    else:
        return np.nan


def S(x):
    if 0 <= x <= 3:
        return 0.08
    elif 3 < x <= 7.5:
        return -0.004389574760 * (x - 3)**3 + 0.029629629630 * (x - 3)**2 + 0.08
    elif 7.5 < x <= 10.5:
        return 0.001171868498 * (x - 7.5)**3 - 0.009071161049 * (x - 7.5)**2 + 0.28
    elif 10.5 < x <= 14:
        return (
            0.004204016117 * (x - 10.5)**3
            - 0.018815867920 * (x - 10.5)**2
            - 0.022786516854 * (x - 10.5)
            + 0.23
        )
    elif 14 < x <= 17.5:
        return -0.005597667638 * (x - 14)**3 + 0.029387755102 * (x - 14)**2 + 0.10
    elif 17.5 < x <= 21.5:
        return 0.0046875 * (x - 17.5)**3 - 0.028125 * (x - 17.5)**2 + 0.22
    elif 21.5 < x <= 24:
        return 0.07
    else:
        return np.nan


x = np.linspace(0, 24, 1000)

y_B = [B(v) for v in x]
y_O = [O(v) for v in x]
y_G = [G(v) for v in x]
y_S = [S(v) for v in x]

y_gesamt = np.array(y_B) + np.array(y_O) + np.array(y_G)


plt.figure(figsize=(12, 6))
plt.plot(x, y_B, label="Vollzeit")
plt.plot(x, y_O, label="Teilzeit")
plt.plot(x, y_G, label="Nicht-Pendler")
plt.plot(x, y_S, label="Gesamt")
plt.plot(x, y_gesamt, label="Aktual Gesamt")

plt.xlim(0, 24)
plt.ylim(0, 1)

plt.xlabel("Zeit")
plt.ylabel("Anteil")
plt.title("Verlauf der vier Graphen")
plt.grid(True)
plt.legend()
plt.show()