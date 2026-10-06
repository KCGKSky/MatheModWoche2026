#########################
## CONFIGURATION FILES ##
#########################


### ALLGEMEIN 

verbose_value = True      # Debug Information in der Console anzeigen
uhrzeit:int = 12          # Uhrzeit der Simulation, 0-24 h
app_nutzer_anteil = 1.0   # Anzahl der Nutzer die eine Preis-Vergleichsapp nutzen
verkehr = 200 # Anzahl von Tanken pro Stunde


### TANKSTELLEN

abstand_AB = 1
abstand_BC = 5
abstand_AC = 5

fluss_A = 0.3
fluss_B = 0.7
fluss_C = 0.0

preis_start_A = 176 # Cent pro Liter
preis_start_B = 175 # Cent pro Liter
preis_start_C = 169 # Cent pro Liter


### KUNDEN

tankvolumen = 120            # Liter
fahrer_geschwindigkeit = 50 # km/h

wendepunkt_vollzeit= 100        # EUR/h Einsparungsrate
wendepunkt_teilzeit = 75        # EUR/h Einsparungsrate
wendepunkt_unbeschaftigt = 50   # EUR/h Einsparungsrate