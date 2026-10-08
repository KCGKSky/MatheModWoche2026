#########################
## CONFIGURATION FILES ##
#########################


### ALLGEMEIN 

verbose_value = False       # Debug Information in der Console anzeigen
uhrzeit:int = 12             # Uhrzeit der Simulation, 0-24 h. Von der Uhrzeit hangt der Stresswert der Kunden ab, was widerum ihre Entscheidung zu wechseln (Aktivierung) beeinflusst.
app_nutzer_anteil = 1.0     # Anzahl der Nutzer die eine Preis-Vergleichsapp nutzen. 
                            # Die App erlaubt es von Tankstele C zu A oder B zu wechseln oder umgekehrt. Fur Wechselvorgange zwischen A und B ist dieser Wert irrelevant

verkehr = 200               # Anzahl von Tankvorgangen pro Stunde


### TANKSTELLEN

abstand_AB = 1  # Abstand der Tankstelle A von B in [km]
abstand_BC = 4  # Abstand der Tankstelle B von C in [km]
abstand_AC = 5  # Abstand der Tankstelle A von C in [km]

fluss_A = 0.45  # Normalstromungen der Kunden als Anteil des Gesamtflusses auf den Strassen, der zur entsprechenden Tankstelle fahrt.
fluss_B = 0.45  # Normalstromungen der Kunden als Anteil des Gesamtflusses auf den Strassen, der zur entsprechenden Tankstelle fahrt.
fluss_C = 0.1   # Normalstromungen der Kunden als Anteil des Gesamtflusses auf den Strassen, der zur entsprechenden Tankstelle fahrt.
                # Sozusagen: Wenn alle Preise gleich waeren und kein Kunde die Tankstelle wechseln wuerde, waeren die Kundschaften gleich den Normalstroemungen

preis_start_A = 200 # Verkaufspreis des Benzins beim Start. wichtig fur nicht_Optimierungsvorgange
preis_start_B = 200 # Verkaufspreis des Benzins beim Start. wichtig fur nicht_Optimierungsvorgange
preis_start_C = 190 # Verkaufspreis des Benzins beim Start. wichtig fur nicht_Optimierungsvorgange

preis_einkauf_A = 110   # Einkaufspreis des Benzins fur die jeweilige Tankstelle
preis_einkauf_B = 110   # Einkaufspreis des Benzins fur die jeweilige Tankstelle
preis_einkauf_C = 105   # Einkaufspreis des Benzins fur die jeweilige Tankstelle

energie_steuer = 65     # Fixabgabe durch die Energie Steuer in [Cent]
co_2_abgabe = 17        # Fixabgabe durch die CO Steuer in [Cent]
mehrwert_steuer = 0.19  # Steuerabgabe durch die Mehrwertsteuer in [%]


### KUNDEN

tankvolumen = 60            # Durchschnittsmenge der Tankmenge pro Tankvorgang in [Liter]
fahrer_geschwindigkeit = 50 # Geschwindigkeit mit der die Kunden die Strecken zwischen den Tankstellen zurucklegen konnen in [km/h]

quote_vollzeit = 0.4        # Verteilung der Kundschaft auf die Normalströmung. Alle Quoten mussen zusammen 1 ergeben.
quote_teilzeit = 0.3        # Verteilung der Kundschaft auf die Normalströmung. Alle Quoten mussen zusammen 1 ergeben.
quote_unbeschaftigt = 0.3   # Verteilung der Kundschaft auf die Normalströmung. Alle Quoten mussen zusammen 1 ergeben.


wendepunkt_vollzeit= 100        # Wendepunkt der Kunden bei der Aktivierungsfunktion. Sozusagen "50% der Kunden wechseln die Tankstelle bei einer Einsparungsrate von X [EUR/Stunde]"
wendepunkt_teilzeit = 75        # Wendepunkt der Kunden bei der Aktivierungsfunktion. Sozusagen "50% der Kunden wechseln die Tankstelle bei einer Einsparungsrate von X [EUR/Stunde]" 
wendepunkt_unbeschaftigt = 50   # Wendepunkt der Kunden bei der Aktivierungsfunktion. Sozusagen "50% der Kunden wechseln die Tankstelle bei einer Einsparungsrate von X [EUR/Stunde]" 



### EVALUATION

preis_start = 0 # Profit_optimum berechnung start
preis_end = 300 # Profit_optimum berechnung ende (Bis wohin schaut man nach)

zeit_fenster:int = 1    # Berechnet mit einem Zeitfenster vorausschauend in Stunden. #KEINE WERTE UNTER 1
                        # bei   zeit_fenster = 24     wird der Preis fur den gesamten Tag optimiert.
                        # bei   zeit_fenster = 1      wird der Preis jede Stunde aufs Optimum eingependelt.
