# Aktion | Syntax | Beispiel
# Ein Element holen | liste[0] | teilchen_arten[1] → "Hefe"
# Länge abfragen | len(liste) | len(analysen)
# Element hinzufügen | liste.append(wert) | teilchen_arten.append("Staub")
# Element entfernen | liste.remove(wert) | teilchen_arten.remove("Hefe")
# Durchgehen (loop) | for element in liste: | for analyse in analysen:
# Nur bestimmte Einträge | if analyse["Typ"] == ... | Filter auf bestimmte Teilchen

analysen = [{"Typ": "Erythrozyt", "Anzahl": 5}, {"Typ": "Hefe", "Anzahl": 8}]
analysen.append({"Typ": "Pollen", "Anzahl": 3})

total = 0

for results in analysen:
    art = results["Typ"]
    amount = results["Anzahl"]
    total += amount
    if art == "Hefe":
        print(f'Typ: {art}')
        print(f'Anzahl: {amount}')
        if amount >= 7: print("Viele Hefe-Zellen") 
        print("-" * 25)
print(f'Gesamte Teilchen: {total}')