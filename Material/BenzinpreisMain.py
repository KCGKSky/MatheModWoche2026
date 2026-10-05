#from: https://kantel.github.io/posts/2023041904_spyder_slider/

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def Tankverhalten(P1,P2,P3):
    #Pi Preis an Tankstelle Ti in Cent
    min12=min(P1,P2)
    min123=min(P1,P2,P3)
    Anteil=[0.0 , 0.0 , 0.0 ]
    if min123 < 250:  # ab 250 Cent tankt niemand
        if P3<min12:
            Anteil[2]=min(max(0.1+(min12-P3)*0.1 , 1.0),0.0)
        Rest=1.0-Anteil[2]
        Anteil[0]=max(min(0.5*Rest+(P2-P1)*0.1*Rest, Rest),0.0)
        Anteil[1]=Rest-Anteil[0]
    return(Anteil)
    
def Gewinn(P1,P2,P3):  #Gewinne durch Umsätze
    Steuer = 65.0  #Cent pro Liter Benzin
    CO2Abgabe = 8.0 # Cent pro Liter Benzin
    Rohbenzinpreis= 100.0 #Cent pro Liter Benzin
    Mwst = 0.14
    Gewinnproliter1 = P1- Steuer - CO2Abgabe - Rohbenzinpreis - Mwst*P1
    Gewinnproliter2 = P2- Steuer - CO2Abgabe - Rohbenzinpreis - Mwst*P2
    Gewinnproliter3 = P3- Steuer - CO2Abgabe - Rohbenzinpreis - Mwst*P3
    Verkaufsanteil=Tankverhalten(P1,P2,P3)
    return([Gewinnproliter1*Verkaufsanteil[0],
           Gewinnproliter2*Verkaufsanteil[1],
           Gewinnproliter3*Verkaufsanteil[2]])

P3 = 300 # so gross dass dort niemand tankt.
Gewinntensor = np.zeros( (6, 6, 2) )
Min = 205.0 # Mindestpreis
Preis1=np.linspace(Min,Min+20,21)
Preis2=np.linspace(Min,Min+20,21)
Preis3=np.linspace(Min-10,Min+10,21)
for i in range(0,6,1):
    P1=Preis1[i]
    for j in range(0,6,1):
        P2=Preis2[j] #P2=Min+j
        Gewinne=Gewinn(P1,P2,P3)
        #print(P1,P2,Gewinne)
        Gewinntensor[i,j,0]=Gewinne[0]        
        Gewinntensor[i,j,1]=Gewinne[1]

print("Gewinntensor")
print("    Preis 2 %11.2f      %11.2f      %11.2f      %11.2f      %11.2f      %11.2f" 
      %(Preis2[0],Preis2[1],Preis2[2],Preis2[3],Preis2[4],Preis2[5]))
print("Preis 1")
for i in [0,1,2,3,4,5]:
    print("%3.2f      [ %3.2f / %3.2f ]  [ %3.2f / %3.2f ]"
    "  [ %3.2f / %3.2f ]  [ %3.2f / %3.2f ]  [ %3.2f / %3.2f ]  [ %3.2f / %3.2f ] " 
          %(Preis1[i],Gewinntensor[i,0,0],Gewinntensor[i,0,1],
            Gewinntensor[i,1,0],Gewinntensor[i,1,1],
            Gewinntensor[i,2,0],Gewinntensor[i,2,1],
            Gewinntensor[i,3,0],Gewinntensor[i,3,1],
            Gewinntensor[i,4,0],Gewinntensor[i,4,1],
            Gewinntensor[i,5,0],Gewinntensor[i,5,1]))
    