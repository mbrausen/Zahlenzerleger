import sys
from rich import print
from rich.console import Console
from rich.table import Table

# Bildschirm initialisieren und löschen
console = Console()
console.clear()

# welchen Potenzen von 2 werden abgebildet?
faktoren = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

abbruch = False
while  not abbruch:
    # Zahl abfragen und in Float wandeln, Fehler abfangen, wenn keine Zahl
    try:
        print('\n\n\n[yellow]Zu zerlegende Zahl:[/] ', end='')
        eingabe = input()
        # Eingabe in Floar wandeln und ggf. Komma ersetzen
        zahl = float(eingabe.replace(',', '.'))
    except ValueError:
        print(f'{eingabe} [bold red]ist keine Zahl![/]')
        sys.exit(1)

    # was ist die größte Zahl, die mit den Potenzen abgebildet werden kann?
    groesste_zahl = 0
    for i in faktoren:
        groesste_zahl += i

    # auf ganze Zahl runden und in Integer wandeln
    zahl = int(round(zahl))

    # ist die Eingabe größer, als das was zerlegt werden kann?
    if abs(zahl) > groesste_zahl:
        print(f'Die eingegebene Zahl ist größer, als die größte Zahl, die zerlegt werden kann ({groesste_zahl}).\n[bold red]Das kann nicht richtig sein![/]')
        sys.exit(1)

    print(f'\nZerlege {zahl}:\n')

    # Variable für Ergebnis initialisieren
    resultat = []

    # Tabelle für Ergebnis initialisieren
    tabelle = Table()
    tabelle.add_column("(-)", justify="center", style="white", no_wrap=True)
    for faktor in faktoren:
        tabelle.add_column(str(faktor), justify="center", style="white", no_wrap=True)

    # Vorzeichen verarbeiten
    if zahl < 0:
        resultat.append('[X]')
        zahl = abs(zahl)
    else:
        resultat.append('[ ]')

    # zerlegen
    for faktor in faktoren:

        if zahl // faktor == 1:
            zahl = zahl - faktor
            resultat.append('[X]')
        else:
            resultat.append('[ ]')

    # Ergebnis ausheben
    tabelle.add_row(*resultat, style="bold")

    console.print(tabelle)
    print('\n\n')
    print('[lightblue]Weitere Zahl zerlegen? (j/n)[/] ', end='')
    weiter = input()
    if weiter.lower() == 'j':
        abbruch = False
        console.clear()
    else:
        abbruch = True
        print('\n\n')
