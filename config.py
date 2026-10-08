#########################
## CONFIGURATION FILES ##
#########################


### ALLGEMEIN 

verbose_value = False      # Debug Information in der Console anzeigen
uhrzeit:int = 7            # Uhrzeit der Simulation, 0-24 h
app_nutzer_anteil = .5    # Anzahl der Nutzer die eine Preis-Vergleichsapp nutzen
verkehr = 200 # Anzahl von Tanken pro Stunde


### TANKSTELLEN

abstand_AB = 1
abstand_BC = 5
abstand_AC = 5

fluss_A = 0.5
fluss_B = 0.5
fluss_C = 0.0

preis_start_A = 200 # Cent pro Liter
preis_start_B = 200 # Cent pro Liter
preis_start_C = 190 # Cent pro Liter

preis_einkauf_A = 60 #Cent
preis_einkauf_B = 60 #Cent
preis_einkauf_C = 60 #Cent

energie_steuer = 65 #Cent
co_2_abgabe = 17 #Cent
mehrwert_steuer = 0.19 #Anteil


### KUNDEN

tankvolumen = 60            # Liter
fahrer_geschwindigkeit = 50 # km/h

quote_vollzeit = 0.4
quote_teilzeit = 0.3
quote_unbeschaftigt = 0.3

wendepunkt_vollzeit= 100        # EUR/h Einsparungsrate
wendepunkt_teilzeit = 75        # EUR/h Einsparungsrate
wendepunkt_unbeschaftigt = 50   # EUR/h Einsparungsrate


### EVALUATION

preis_start = 0 # Profit_optimum berechnung start
preis_end = 400 # Profit_optimum berechnung ende (Bis wohin schaut man nach)