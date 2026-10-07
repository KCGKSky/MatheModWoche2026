import numpy as np
import matplotlib.pyplot as plt
import config as config
import bibliothek as bib


def plot_profit_over_uhrzeit(kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val):
    # for Tankstelle A, B und C
    tabelle_A, tabelle_B, tabelle_C = [0]*end_val, [0]*end_val, [0]*end_val
    for sim in range(start_val, end_val, 1):
        tabelle_A[sim], tabelle_B[sim], tabelle_C[sim] = bib.gesamt_profit_volumen(kunden=kunden,
                                 tankstelle_A=tankstelle_A,
                                 tankstelle_B=tankstelle_B,
                                 tankstelle_C=tankstelle_C,
                                 uhrzeit=sim,
                                 verbose=False
                                 )
        
    plt.plot(tabelle_A, label="Tankstelle A")
    plt.plot(tabelle_B, label="Tankstelle B")
    plt.plot(tabelle_C, label="Tankstelle C")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return 0




#y = eingependelte_preise = bib.optimal_konstellation(80, kunde=kunde, tankstelle_A=tankstelle_A, tankstelle_B=tankstelle_B, tankstelle_C=tankstelle_C, verbose=False)
#x = np.arange(0, 24, 0.1)