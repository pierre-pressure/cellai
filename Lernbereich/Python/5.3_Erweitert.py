analysen = [
    {"Typ": "Hefe", "Anzahl": 8},
    {"Typ": "Erythrozyt", "Anzahl": 5},
    {"Typ": "Hefe", "Anzahl": 3},
]


def gesamtmenge_typ(liste, typ):
    gesamt = 0
    gefunden = False
    for i in liste:
        if i["Typ"] == typ:
            gesamt += i["Anzahl"]
            gefunden = True
    if not gefunden:
        return None
    return gesamt


typ = ""
print(gesamtmenge_typ(analysen, typ))


analyse = [{"Typ": "Hefe", "Anzahl": 8}, {"Typ": "Erythrozyt", "Anzahl": 5}]


def finde_analyse(liste, typ):
    for eintrag in liste:
        if eintrag["Typ"] == typ:
            return eintrag
    return None


such_typ = "Pollen"
ergebnis = finde_analyse(analysen, such_typ)

if ergebnis is None:
    print("Typ nicht gefunden")
else:
    print(f"Typ: {ergebnis['Typ']} – Anzahl: {ergebnis['Anzahl']}")
