analyse = {"Typ": "Erythrozyt", "Anzahl": 5, "Genauigkeit": 81.5, "Angepasst": False}

accuracy = analyse["Genauigkeit"]
if accuracy >= 95:
    print("Top-Ergebnis!")
elif accuracy >= 90:
    print("Sehr gut")
elif accuracy >= 80:
    print("Akzeptabel")
else: print("Ungenügend - bitte wiederholen")

if analyse["Anzahl"] < 5: print("Sehr wenige Teilchen erkannt!")

print("Bild wurde angepasst") if analyse["Angepasst"] else print("Bild wurde nicht angepasst")


analysen = [
    {"Typ": "Erythrozyt", "Anzahl": 5, "Genauigkeit": 92.5, "Angepasst": True},
    {"Typ": "Hefe", "Anzahl": 3, "Genauigkeit": 78.0, "Angepasst": False},
    {"Typ": "Erythrozyt", "Anzahl": 9, "Genauigkeit": 96.4, "Angepasst": True}
]
analyzed = 0

for analyze in analysen:
    typ = analyze["Typ"]
    anzahl = analyze["Anzahl"]
    genauigkeit = analyze["Genauigkeit"]
    angepasst = analyze["Angepasst"]
    corrected = "Ja" if angepasst else "Nein"
    if genauigkeit >= 95:
        rating = "Top"
    elif genauigkeit >= 90:
        rating = "Gut"
    elif genauigkeit >= 80:
        rating = "Okay"
    else: rating = "Wiederholen empfohlen"
    analyzed += 1


    print(f'Typ: {typ}')
    print(f'Anzahl: {anzahl}')
    print(f'Genauigkeit: {genauigkeit}%')
    print(f'Bild angepasst: {corrected}')
    print(f'Bewertung: {rating}')

print(f'Durchgeführte Analysen: {analyzed}')