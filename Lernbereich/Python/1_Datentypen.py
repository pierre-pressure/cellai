cell_type = "Hefezellen"
cell_amount = 23
accuracy = 94.3
img_corrected = True

print(f"Erkannt: {cell_type}")
print(f"Anzahl: {cell_amount}")
print(f"Genauigkeit: {accuracy}%")
print(f"Bild angepasst: {img_corrected}")

results = [{"Typ": "Hefe", "Anzahl": 12}, {"Typ": "Erythrozyt", "Anzahl": 8}] # liste mit zwei dicts

for i in results: # iterriere durch die liste
    typ = i["Typ"] # typ = value von key "Typ"
    anzahl = i["Anzahl"] # anzahl = value von key "Anzahl"
    print(f'Typ: {typ} - Anzahl: {anzahl}')

analysen = [
    {"Typ": "Hefe", "Anzahl": 14, "Genauigkeit": 93.2, "Angepasst": True},
    {"Typ": "Erythrozyt", "Anzahl": 9, "Genauigkeit": 89.7, "Angepasst": False},
    {"Typ": "Hefe", "Anzahl": 17, "Genauigkeit": 95.5, "Angepasst": True}
]

menge = 0
for analyze in analysen:
    art = analyze["Typ"]
    amount = analyze["Anzahl"]
    genauigkeit = analyze["Genauigkeit"]
    angepasst = analyze["Angepasst"]
    print(f'Typ: {art}')
    print(f'Anzahl: {amount}')
    menge += analyze["Anzahl"]
    print(f'Genauigkeit: {genauigkeit}%')
    angepasst_text = "Ja" if angepasst else "Nein"
    print(f'Bild angepasst: {angepasst_text}')
print(f'Gesamte Teilchen: {menge}')