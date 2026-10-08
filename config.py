#########################
## CONFIGURATION FILES ##
#########################


##     |\__/,|   (`\   ##
##   _.|o o  |_   ) )  ##
## -(((---(((--------  ##


### ALLGEMEIN ###

verbose_value = False       # Mehr debug Information in der Console anzeigen
uhrzeit:int = 12            # Uhrzeit der Simulation, 0-24 h. Von der Uhrzeit hangt der Stresswert der Kunden ab, was widerum ihre Entscheidung zu wechseln (Aktivierung) beeinflusst.
app_nutzer_anteil = 0.5     # Anzahl der Nutzer die eine Preis-Vergleichsapp nutzen.
                            # Die App erlaubt es von Tankstele C zu A oder B zu wechseln oder umgekehrt. Fur Wechselvorgange zwischen A und B ist dieser Wert irrelevant

verkehr = 1000              # Anzahl von Tankvorgangen am Tag an ALLEN TANKSTELLEN ZUSAMMEN! [Tankvorgang/Tag]


### TANKSTELLEN ###

abstand_AB = 1  # Abstand der Tankstelle A von B in [km]
abstand_BC = 4  # Abstand der Tankstelle B von C in [km]
abstand_AC = 5  # Abstand der Tankstelle A von C in [km]
                # Dreiecksungleichung beachten ist optional.

fluss_A = 0.45  # Normalstromungen der Kunden als Anteil des Gesamtflusses auf den Strassen, der zur entsprechenden Tankstelle fahrt.
fluss_B = 0.45  # Normalstromungen der Kunden als Anteil des Gesamtflusses auf den Strassen, der zur entsprechenden Tankstelle fahrt.
fluss_C = 0.1   # Normalstromungen der Kunden als Anteil des Gesamtflusses auf den Strassen, der zur entsprechenden Tankstelle fahrt.
                # Sozusagen: Wenn alle Preise gleich waeren und kein Kunde die Tankstelle wechseln wuerde, waeren die Kundschaften gleich den Normalstroemungen
                # Alle Flusse mussen ZUSAMMEN 1 ergeben! Sonst

preis_start_A = 240 # Verkaufspreis des Benzins beim Start. wichtig fur nicht_Optimierungsvorgange
preis_start_B = 240 # Verkaufspreis des Benzins beim Start. wichtig fur nicht_Optimierungsvorgange
preis_start_C = 235 # Verkaufspreis des Benzins beim Start. wichtig fur nicht_Optimierungsvorgange

## Einstellungen fur Benzinpreise
preis_einkauf_A = 110   # Einkaufspreis des Benzins fur die jeweilige Tankstelle
preis_einkauf_B = 110   # Einkaufspreis des Benzins fur die jeweilige Tankstelle
preis_einkauf_C = 105   # Einkaufspreis des Benzins fur die jeweilige Tankstelle

energie_steuer = 65     # Fixabgabe durch die Energie Steuer in [Cent]
co_2_abgabe = 17        # Fixabgabe durch die CO Steuer in [Cent]
mehrwert_steuer = 0.19  # Steuerabgabe durch die Mehrwertsteuer in [%]


### KUNDEN ###

tankvolumen = 60            # Durchschnittsmenge der Tankmenge pro Tankvorgang in [Liter]
fahrer_geschwindigkeit = 50 # Geschwindigkeit mit der die Kunden die Strecken zwischen den Tankstellen zurucklegen konnen in [km/h]

quote_vollzeit = 0.4        # Verteilung der Kundschaft auf die Normalströmung. Alle Quoten mussen zusammen 1 ergeben.
quote_teilzeit = 0.3        # Verteilung der Kundschaft auf die Normalströmung. Alle Quoten mussen zusammen 1 ergeben.
quote_unbeschaftigt = 0.3   # Verteilung der Kundschaft auf die Normalströmung. Alle Quoten mussen zusammen 1 ergeben.


wendepunkt_vollzeit= 60         # Wendepunkt der Kunden bei der Aktivierungsfunktion. Sozusagen "50% der Kunden wechseln die Tankstelle bei einer Einsparungsrate von X [EUR/Stunde]"
wendepunkt_teilzeit = 45        # Wendepunkt der Kunden bei der Aktivierungsfunktion. Sozusagen "50% der Kunden wechseln die Tankstelle bei einer Einsparungsrate von X [EUR/Stunde]"
wendepunkt_unbeschaftigt = 30   # Wendepunkt der Kunden bei der Aktivierungsfunktion. Sozusagen "50% der Kunden wechseln die Tankstelle bei einer Einsparungsrate von X [EUR/Stunde]"


### EVALUATION SETTINGS (nicht relevant) ###

preis_start = 0 # Der Startwert bei der Berechnung der Benzinpreistabelle zur Feststellung des Optimalen Profiterschlags
preis_end = 300 # Der Startwert bei der Berechnung der Benzinpreistabelle zur Feststellung des Optimalen Profiterschlags (Sozusagen: "Bis wohin schaut man nach")

zeit_fenster:int = 1    # Berechnet mit einem Zeitfenster vorausschauend in Stunden. #KEINE WERTE UNTER 1
                        # bei   zeit_fenster = 24     wird der Preis fur den gesamten Tag optimiert. (SEHR RECHENINTENSIV, d.h Kaffeepause einplanen)
                        # bei   zeit_fenster = 1      wird der Preis jede Stunde aufs Optimum eingependelt.
