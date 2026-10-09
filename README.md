# MatheModWoche 2026 – Benzinpreiskampf

Das Projekt ist während der **Mathematik-Modellierungswoche 2026** in Kassel-Fuldatal in Hessen entstanden. Die Modellierungswoche wurde vom **Zentrum für Mathematik e. V.** organisiert.
Wir bedanken uns herzlich, dass wir teilnehmen durften und uns eine Woche lang mit dieser Aufgabe beschäftigen konnten.

## Vorstellung

Die Modellierungswoche fand an der Reinhardswaldschule in Fuldatal, Hessen mit insgesamt 40 mathematikbegabten Schüler/innen, welche in Acht Arbeitsgruppen aufgeteilt wurden, statt.
Dabei hat jede Gruppe ein Optimierungsproblem aus der Wirtschaft und Industrie mithilfe von mathematischen Ansätzen und Python gelöst, und anschließend am Ende der Woche in einem 20 min Vortrag im Plenum präsentiert.

Wir haben innerhalb der Modellierungswoche die Aufgabe der **Benzinpreisoptimierung: "Benzinpreiskampf"** bearbeitet.

In `Material/Aufgaben2026` finden sie die Optimierungsprobleme der anderen Arbeitsgruppen.

In diesem Projekt beschäftigen wir uns mit der Frage der **Benzinpreisoptimierung** bei konkurrierenden Tankstellen. Wir haben dafür ein eigenes mathematisches Modell entwickelt, mit dem wir untersuchen, wie Kundinnen und Kunden auf unterschiedliche Benzinpreise reagieren und welche Preise für die Tankstellen besonders profitabel sein könnten.

In `Presentation Material/benzinpreiskampf_presentation.pdf` finden sie eine anschauliche Präsentation, die den Sachverhalt darstellt.

## Problemdarstellung

Wir betrachten drei Tankstellen: A, B und C. Sie unterscheiden sich unter anderem durch ihre Einkaufspreise und die Entfernung zueinander. Kundinnen und Kunden haben unterschiedliche Gewohnheiten und entscheiden nicht alle gleich: Manche bleiben bei ihrer gewohnten Tankstelle, andere vergleichen Preise und nehmen dafür auch einen Umweg in Kauf.

Diese Entscheidungen versuchen wir im Modell nachzubilden. Dabei spielen zum Beispiel die Uhrzeit, das Verkehrsaufkommen, die Nutzung einer Preisvergleichs-App und unterschiedliche Kundengruppen eine Rolle. Anschließend berechnet das Programm, wie sich die Kundenverteilung und die Gewinne verändern, wenn die Tankstellen ihre Preise anpassen.

Die Ergebnisse der Modellsimulation werden vom interaktiven Python-Program als `matplotlib` Diagramme geplotted und die bedeutungsvollen Informationen in der Konsole ausgegeben.

## Dateibedeutung

| Datei/Ordner | Beschreibung |
| --- | --- |
| `main.py` | Selbsterklärend |
| `config.py` | Hier lassen sich die Werte des Modells verändern, zum Beispiel Preise, Abstände und Kundenanteile. |
| `bibliothek.py` | Eigentliche Modelllogik, etwa wie die Berechnung von Kundenverhalten, Gewinnen und Preisen. |
| `draw_utils.py` | Visualisierungsfunktionen |
| `Material/` | Uns zur Verfügung gegebenes Material |
| `Presentation Material/` | Weitere Präsentationsmaterialien. |

## Anpassung der Modellierungswerte in `config.py`

Die Konfiguration befindet sich in `config.py`. Die Parameter werden innerhalb der Konfig-Datei nochmal genauer erklärt.\
**Sie haben freie Hand selber mit dem Modell zu experimentieren** und eigene Werte festzulegen.

- `uhrzeit`: Zu welcher Uhrzeit die Simulation betrachtet wird.
- `app_nutzer_anteil`: Wie viele Kundinnen und Kunden eine Preisvergleichs-App nutzen.
- `verkehr`: Wie viele Tankvorgänge pro Tag insgesamt angenommen werden.
- `abstand_AB`, `abstand_BC`, `abstand_AC`: Die Entfernungen zwischen den Tankstellen.
- `fluss_A`, `fluss_B`, `fluss_C`: Wie sich die Kundschaft normalerweise auf die drei Tankstellen verteilt.
- `preis_start_A`, `preis_start_B`, `preis_start_C`: Die anfänglichen Verkaufspreise.
- `preis_einkauf_A`, `preis_einkauf_B`, `preis_einkauf_C`: Die Einkaufspreise der Tankstellen.
- `tankvolumen`: Die durchschnittlich getankte Benzinmenge pro Tankvorgang.
- `quote_vollzeit`, `quote_teilzeit`, `quote_unbeschaeftigt`: Die Anteile der verschiedenen Kundengruppen.
- `zeit_fenster`: Wie weit die Optimierung in die Zukunft schaut.


## Installation und Start

Ihr braucht Python 3 sowie die Bibliotheken `numpy` und `matplotlib`.

Ladet zunächst die Github Repository herunter:

```bash
git clone https://github.com/KCGKSky/MatheModWoche2026.git
cd MatheModWoche2026
```

Installiert anschließend die benötigten Bibliotheken:

```bash
python -m pip install numpy matplotlib
```

Dann könnt ihr das Programm starten:

```bash
python main.py
```

Falls der Befehl `python` bei euch nicht funktioniert, probiert `python3`.

## Ein Hinweis zum Modell

Natürlich bildet unser Modell die Wirklichkeit nicht vollständig ab. Das Verhalten von Menschen und die Preisgestaltung an Tankstellen sind deutlich komplexer, als es sich mit einigen Parametern darstellen lässt. Die Ergebnisse hängen deshalb stark von den Annahmen und Einstellungen ab. Das Modell soll vor allem helfen, Zusammenhänge zu untersuchen und verschiedene Szenarien miteinander zu vergleichen.

**DISCLAIMER:** Der Code ist zwar nicht schön, aber er wurde *ohne KI* geschrieben.
Jede Zeile Code ist von einem von uns geschrieben worden. Insgesamt steckt hinter dem Projekt ein Aufwand von circa 8-10 Stunden Arbeit an 4 Tagen von 5 Gruppenmitgliedern.\
Das ergibt circa. **160 Arbeitsstunden.** \
Auch haben wir viele neue Kenntnisse innerhalb der Woche erlernt.

**Das heißt:** Der Code ist das Endprodukt einer einwöchigen, anspruchsvollen Gruppenarbeit und ist von unserem unmittelbaren Lernprozess gezeichnet. 

## Danke

Die Mathematik-Modellierungswoche 2026 wurde vom **Zentrum für Mathematik e. V.** organisiert. Wir bedanken uns herzlich, dass wir teilnehmen durften und uns eine Woche lang mit dieser Aufgabe beschäftigen konnten.
