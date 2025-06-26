analysen = [
    {"Typ": "Hefe", "Anzahl": 8},
    {"Typ": "Erythrozyt", "Anzahl": 5},
    {"Typ": "Hefe", "Anzahl": 3},
    {"Typ": "Pollen", "Anzahl": 9},
    {"Typ": "Erythrozyt", "Anzahl": 6}
]

summen = {}

for i in analysen:
    art = i["Typ"]
    amount = i["Anzahl"]
    if art not in summen: summen[art] = amount # schreibt '{art: amount}' z.B. "Hefe": 11
    else: summen[art] += amount

print(f'Analyseergebnisse:')
for typ, anzahl in summen.items(): # iterrieren mit key-value
    print(f"- {typ}: {anzahl} Zellen")


# Übung Doppel-for-Iteration
# dict.items(): Schlüssel und Werte (→ key, value)
# dict.keys(): Nur die Schlüssel
# dict.values(): Nur die Werte
zutaten = {
    "Mehl": "500g",
    "Wasser": "300ml",
    "Hefe": "1 Würfel",
    "Salz": "1 TL"
}

for ingredient, amount in zutaten.items():
    print(f'Zutat: {ingredient} - Menge: {amount}')