import numpy as np
import matplotlib.pyplot as plt
import config as config
import bibliothek as bib


def plot_profit_over_uhrzeit(kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val, verbose):
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
    # Only to display Info
    bib.profit_volumen(kunde=kunden[0],
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=verbose
                    )
        
    plt.plot(tabelle_A, label="Tankstelle A")
    plt.plot(tabelle_B, label="Tankstelle B")
    plt.plot(tabelle_C, label="Tankstelle C")
    plt.title("Feste Preise")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True)



def plot_profit_over_uhrzeit_optimized(kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val, verbose):
    # for Tankstelle A, B und C
    tabelle_A, tabelle_B, tabelle_C = [0]*end_val, [0]*end_val, [0]*end_val
    for sim in range(start_val, end_val, 1):
        tankstelle_A.preis_verkauf, tankstelle_B.preis_verkauf, tankstelle_C.preis_verkauf = bib.optimal_konstellation(kunden, tankstelle_A, tankstelle_B, tankstelle_C)
        tabelle_A[sim], tabelle_B[sim], tabelle_C[sim] = bib.gesamt_profit_volumen(kunden=kunden,
                                 tankstelle_A=tankstelle_A,
                                 tankstelle_B=tankstelle_B,
                                 tankstelle_C=tankstelle_C,
                                 uhrzeit=sim,
                                 verbose=False
                                 )

    tankstelle_A.preis_verkauf = config.preis_start_A
    tankstelle_B.preis_verkauf = config.preis_start_B
    tankstelle_C.preis_verkauf = config.preis_start_C
    #only to display info
    bib.profit_volumen(kunde=kunden[0],
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=verbose
                    )

    plt.plot(tabelle_A, label="Tankstelle A")
    plt.plot(tabelle_B, label="Tankstelle B")
    plt.plot(tabelle_C, label="Tankstelle C")
    plt.title("Optimale Preise")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True)



def plot_preis_zu_profit(kunden, tankstelle_A, tankstelle_B, tankstelle_C, verbose=False):
    tabelle = bib.preis_zu_profit_tabelle(kunden=kunden,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=verbose)

    plt.plot(tabelle[0], label="Tankstelle A")
    plt.plot(tabelle[1], label="Tankstelle B")
    plt.plot(tabelle[2], label="Tankstelle C")
    plt.xlabel("Preis [C/L]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True)



def plot_stress_function(kunden):
    stress = [0]*24
    for i in range(0, 24, 1):
        stress[i] = kunden[0].stress_funktion(i)

    plt.plot(stress, label="Stress im Verkehr")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Stress")
    plt.legend()
    plt.grid(True)
          

#y = eingependelte_preise = bib.optimal_konstellation(80, kunde=kunde, tankstelle_A=tankstelle_A, tankstelle_B=tankstelle_B, tankstelle_C=tankstelle_C, verbose=False)
#x = np.arange(0, 24, 0.1)