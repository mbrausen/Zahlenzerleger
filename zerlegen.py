import sys

# Zahl abfragen und in Float wandeln, Fehler abfangen, wenn keine Zahl
try:
    eingabe = input('\n\n\nZu zerlegende Zahl: ')
    # Eingabe in Floar wandeln und ggf. Komma ersetzen
    zahl = float(eingabe.replace(',', '.'))
except ValueError:
    print('Keine Zahl eingegeben!')
    sys.exit(1)

# welchen Potenzen von 2 werden abgebildet?
faktoren = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

# was ist die größte Zahl, die mit den Potenzen abgebildet werden kann?
groesste_zahl = 0
for i in faktoren:
    groesste_zahl += i

# auf ganze Zahl runden und in Integer wandeln
zahl = int(round(zahl))

# ist die Eingabe größer, als das was zerlegt werden kann?
if abs(zahl) > groesste_zahl:
    print(f'Die eingegebene Zahl ist größer, als die größte Zahl, die zerlegt werden kann ({groesste_zahl}).\nDas kann nicht richtig sein!')
    sys.exit(1)

print(f'\nZerlege {zahl}.\n')

# Variable für Ergebnis initialisieren
resultat = []

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
print('-'*43)
print("(-) 512 256 128  64  32  16  8   4   2   1")
print(' '.join(resultat))
print('-'*43)
print('\n\n')
