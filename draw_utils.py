import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider
import config as config
import bibliothek as bib


def plot_profit_over_uhrzeit_fest(figure_i, kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val, verbose):
    # for Tankstelle A, B und C
    def berechne_tabellen(mod_var):
        tabelle_A, tabelle_B, tabelle_C = [0]*end_val, [0]*end_val, [0]*end_val
        for sim in range(start_val, end_val, 1):
            tabelle_A[sim], tabelle_B[sim], tabelle_C[sim] = bib.gesamt_profit_volumen(kunden=kunden,
                                 tankstelle_A=tankstelle_A,
                                 tankstelle_B=tankstelle_B,
                                 tankstelle_C=tankstelle_C,
                                 uhrzeit=sim,
                                 verbose=False,
                                 app_nutzer_anteil=mod_var
                                 )
        return tabelle_A, tabelle_B, tabelle_C
    # Only to display Info
    bib.profit_volumen(kunde=kunden[0],
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=verbose
                    )

  
    fig = plt.figure(figure_i)
    ax = fig.add_subplot(111)

    tab_A, tab_B, tab_C = berechne_tabellen(config.app_nutzer_anteil)
    ax.plot(tab_A, label="Tankstelle A Verkaufspreis: "+str(config.preis_start_A), color="blue", linewidth=2, linestyle="solid")
    ax.plot(tab_B, label="Tankstelle B Verkaufspreis: "+str(config.preis_start_B), color="orange", linewidth=2, linestyle="solid")
    ax.plot(tab_C, label="Tankstelle C Verkaufspreis: "+str(config.preis_start_C), color="black", linewidth=2, linestyle="dashed")
    
    plt.title("Profit bei festen Benzinpreisen")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")
    


def plot_profit_over_uhrzeit_optimized(figure_i, kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val, verbose):
    # for Tankstelle A, B und C
    tabelle_A, tabelle_B, tabelle_C = [0]*end_val, [0]*end_val, [0]*end_val
    for sim in range(start_val, end_val, 1):
        tankstelle_A.preis_verkauf, tankstelle_B.preis_verkauf, tankstelle_C.preis_verkauf = bib.optimal_konstellation(kunden, tankstelle_A, tankstelle_B, tankstelle_C, uhrzeit_start=sim, uhrzeit_end=sim)
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
    
    plt.figure(figure_i)
    plt.plot(tabelle_A, label="Tankstelle A Einkaufspreis: "+str(config.preis_einkauf_A), color="blue", linewidth=2, linestyle="solid")
    plt.plot(tabelle_B, label="Tankstelle B Einkaufspreis: "+str(config.preis_einkauf_B), color="orange", linewidth=2, linestyle="solid")
    plt.plot(tabelle_C, label="Tankstelle C Einkaufspreis: "+str(config.preis_einkauf_C), color="black", linewidth=2, linestyle="dashed")
    plt.title("Profit bei eingependelten Preisen")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")
    



def plot_preis_zu_profit(figure_i, kunden, tankstelle_A, tankstelle_B, tankstelle_C, uhrzeit, verbose=False):
    tabelle_A, tabelle_B, tabelle_C = bib.preis_zu_profit_tabelle(kunden=kunden,
                                          uhrzeit=uhrzeit,
                                  tankstelle_A=tankstelle_A,
                                  tankstelle_B=tankstelle_B,
                                  tankstelle_C=tankstelle_C,
                                  verbose=verbose)
    plt.figure(figure_i)
    plt.plot(tabelle_A, label="Tankstelle A", color="blue", linewidth=2, linestyle="solid")
    plt.plot(tabelle_B, label="Tankstelle B", color="orange", linewidth=2, linestyle="solid")
    plt.plot(tabelle_C, label="Tankstelle C", color="black", linewidth=2, linestyle="dashed")
    plt.title("Profiterwarung bei Verkaufspreisen [x]")
    plt.xlabel("Preis [C/L]")
    plt.ylabel("Profit [EUR]")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")



def plot_stress_function(figure_i, kunden):
    stress = [0]*24
    for i in range(0, 24, 1):
        stress[i] = kunden[0].stress_funktion(i)

    plt.figure(figure_i)
    plt.plot(stress, label="Stress im Verkehr", color="black", linewidth=2, linestyle="dashed")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Stress")
    plt.title("Stressfunktion")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")

def plot_preis_over_uhrzeit_optimized(figure_i, kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val, verbose):
    # for Tankstelle A, B und C
    tabelle_A, tabelle_B, tabelle_C = [0]*end_val, [0]*end_val, [0]*end_val
    for sim in range(start_val, end_val, 1):
        tabelle_A[sim], tabelle_B[sim], tabelle_C[sim] = bib.optimal_konstellation(kunden, tankstelle_A, tankstelle_B, tankstelle_C, uhrzeit_start=sim, uhrzeit_end=sim)

    #only to display info
    bib.profit_volumen(kunde=kunden[0],
                    tankstelle_A=tankstelle_A,
                    tankstelle_B=tankstelle_B,
                    tankstelle_C=tankstelle_C,
                    verbose=verbose
                    )
    
    plt.figure(figure_i)
    plt.plot(tabelle_A, label="Tankstelle A", color="blue", linewidth=2, linestyle="solid")
    plt.plot(tabelle_B, label="Tankstelle B", color="orange", linewidth=2, linestyle="solid")
    plt.plot(tabelle_C, label="Tankstelle C", color="black", linewidth=2, linestyle="dashed")
    plt.title("Eingependelte Benzinpreise")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Benzinpreis [C/L]")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")

def plot_konstellations_verlauf(figure_i, kunden, tankstelle_A, tankstelle_B, tankstelle_C, start_val, end_val, verbose):
    konstellationen = bib.optimal_konstellation(kunden, tankstelle_A, tankstelle_B, tankstelle_C, uhrzeit_start=start_val, uhrzeit_end=end_val, verlauf=True)
    konstellation_A = [konstellationen[i][1] for i in range(len(konstellationen))]
    konstellation_B = [konstellationen[i][2] for i in range(len(konstellationen))]
    konstellation_C = [konstellationen[i][3] for i in range(len(konstellationen))]
    plt.figure(figure_i)
    plt.plot(konstellation_A, label="Tankstelle A", color="blue", linewidth=2, linestyle="solid")
    plt.plot(konstellation_B, label="Tankstelle B", color="orange", linewidth=2, linestyle="solid")
    plt.plot(konstellation_C, label="Tankstelle C", color="black", linewidth=2, linestyle="dashed")

    plt.title("Verlauf der optimalen Konstellation")
    plt.xlabel("KonstellationsNr")
    plt.ylabel("Preis [C/L]")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")


def plot_aktivierung(figure_i, kunden, end_val, stress = 1):
    x = range(end_val)
    
    aktivierung_A, aktivierung_B, aktivierung_C = [0]*end_val, [0]*end_val, [0]*end_val
    for i in x:
        aktivierung_A[i] = kunden[0].aktivierung(i, stress)
        aktivierung_B[i] = kunden[1].aktivierung(i, stress)
        aktivierung_C[i] = kunden[2].aktivierung(i, stress)

    plt.figure(figure_i)
    plt.plot(aktivierung_A, label="Aktivierungsfunktion Vollzeit", color="blue", linewidth=2, linestyle="solid")
    plt.plot(aktivierung_B, label="Aktivierungsfunktion Teilzeit", color="orange", linewidth=2, linestyle="solid")
    plt.plot(aktivierung_C, label="Aktivierungsfunktion Unbeschaftigt", color="black", linewidth=2, linestyle="dashed")

    plt.title("Aktivierung der Kunden / Stress = " + str(stress))
    plt.xlabel("Ersparnis pro Zeit [EUR/h]")
    plt.ylabel("Anteil der Aktivierten")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")

def plot_einkommensverteilung(figure_i, end_val):
    def einkommen(x):
        return np.exp(-(np.log(x) - np.log(54066))**2 / (2 * 0.5925**2)) / (x * 0.5925 * np.sqrt(2 * np.pi))
    x = range(1, end_val)
    einkommen_tabelle = [0]*end_val
    for i in x:
        einkommen_tabelle[i] = einkommen(i)
        
    plt.figure(figure_i)
    plt.plot(einkommen_tabelle, label="Prozent der Bevolkerung Deutschland", color="black", linewidth=2, linestyle="dashed")
    plt.title("Einkommensverteilung")
    plt.xlabel("Brutto pro Jahr")
    plt.ylabel("Prozent Bevolkerung")
    plt.grid(True, "major", linestyle="dashed")
    

def plot_verkehrs_vorkommen(figure_i):
    x = range(0, 24)
    verkehr_vorkommen_tabelle = [0]*24
    for i in x:
        verkehr_vorkommen_tabelle[i] = bib.verkehrs_vorkommen(i)
        
    plt.figure(figure_i)
    plt.plot(verkehr_vorkommen_tabelle, label="Anteil der Tankvorgange", color="black", linewidth=2, linestyle="dashed")
    plt.title("Verteilung der durchschnittlichen Tankvorgange")
    plt.xlabel("Uhrzeit [h]")
    plt.ylabel("Anteil der Tankvorgange")
    plt.legend()
    plt.grid(True, "major", linestyle="dashed")