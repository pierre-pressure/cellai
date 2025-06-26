analysen = [
    {"Typ": "Erythrozyt", "Anzahl": 5},
    {"Typ": "Hefe", "Anzahl": 8},
    {"Typ": "Hefe", "Anzahl": 3},
    {"Typ": "Pollen", "Anzahl": 4},
]

yeast_counter = 0
yeast_amount = 0
for i in analysen:
    yeast = i["Typ"]
    if yeast == "Hefe":
        yeast_counter += 1
        yeast_amount += i["Anzahl"]
print(f"Hefe-Analysen: {yeast_counter}")
print(f"Erkannte Hefe-Zellen: {yeast_amount}")

for j in analysen:
    art = j["Typ"]
    menge = j["Anzahl"]
    if art == "Pollen": 
        analysen.remove(j)
        break # j wird entfernt und for loop wird beendet
    print(f"Teilchentyp: {art}")
    print(f"Anzahl: {menge}")
