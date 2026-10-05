#from: https://kantel.github.io/posts/2023041904_spyder_slider/

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(x, a, b, c , d):
    return a*np.sin(2*np.pi*(x-c)/b)+d

#Lesen der Daten aus Datei TageslängenDA2025
file =  open('TageslängenDA2025.txt','r')  # open braucht den genauen Pfad ab working directory
Tageslängen = []   #erzeugt leeren Vektor
for line in file:
    Tageslängen.append(float(line))   # verlängert den Vektor und wandelt den gelesenen Text in float um
#Tageslängen = f.readlines()
file.close()

print('Ändere die Parameter $a$,$b$,$c$ und $d$ über die Schieberegler, um den blauen Graph an die rote Kurve anzupassen.')
print('Eine gute Anpassung erhält man für $a=4.1$')
print('Jahresdauer $b=364.75$')
print("Tag der Frühjahrs-Tag-und-Nacht-Gleiche $c=80$ ")
print('mittlere Tagesdauer $d=12.35$. Wegen der elliptischen Erdbahn ist der Winter auf der Nordhalbkugel kürzer')

fig, ax = plt.subplots(figsize = (6, 6))
plt.title(r"$y = a*sin(2\pi(x-c)/b)+d$")
plt.subplots_adjust(left = 0.12, bottom = 0.3)
plt.xlim(0, 365)
plt.ylim(-1, 25)
plt.xlabel(r"$t$ in [d]")
plt.ylabel(r"Tageslänge in [h]", rotation = 90)

x = np.arange(0, 400, 0.1) #erzeugt einen Vektor von bis Schrittweite
y, = plt.plot(x, f(x, 6, 300, 30, 12), 'b-', lw = 1)
x2 = np.arange(0, 365, 1)
data, = plt.plot(x2,Tageslängen,'r:',lw = 1)

# x- und y-Position, Länge und Höhe der Slider im Plot festlegen
xyA = plt.axes([0.1, 0.17, 0.8, 0.03])
xyB = plt.axes([0.1, 0.12, 0.8, 0.03])
xyC = plt.axes([0.1, 0.07, 0.8, 0.03])
xyD = plt.axes([0.1, 0.02, 0.8, 0.03])

# Slider-Objekte erzeugen
# Slidername=Slider()
sldA = Slider(xyA, "a",   0.0, 14.0, valinit = 6, valstep = 0.1)
sldB = Slider(xyB, "b",   0.0,  400.0, valinit = 300, valstep = 0.1)
sldC = Slider(xyC, "c", 0, 365.0, valinit = 30, valstep = 1.0)
sldD = Slider(xyD, "d", 10.0, 14.0, valinit = 12, valstep = 0.01)

# Slider Update
def update(val):
    a = sldA.val
    b = sldB.val
    c = sldC.val
    d = sldD.val
    y.set_data(x, f(x, a, b, c, d))
    
# Änderungen abfragen
sldA.on_changed(update)
sldB.on_changed(update)
sldC.on_changed(update)
sldD.on_changed(update)

ax.grid(True)
plt.show()