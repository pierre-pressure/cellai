def analyse_durchfuehren(anzahl, typ):

    match typ:
        case "Hefe":
            return f"Typ: Hefe erkannt - Anzahl: {anzahl}"
        case "Erythrozyt":
            return f"Typ: Erythrozyt erkannt - Anzahl: {anzahl}"
        case "Pollen":
            return f"Typ: Pollen erkannt - Anzahl: {anzahl}"
        case _:
            return f"Unbekannter Zelltyp"


print(analyse_durchfuehren(12, "Hefe"))


def lese_anzahl():
    try:
        anzahl = float(input("Bitte gib die Zellanzahl ein: "))
        return anzahl
    except ValueError:
        anzahl = None
        print("Bitte gib eine Zahl an.")


print(f"Anzahl: {lese_anzahl()}")


analysen_liste = [
    {"Typ": "Hefe", "Anzahl": 8},
    {"Typ": "Erythrozyt", "Anzahl": 5},
    {"Typ": "Hefe", "Anzahl": 3},
]


def analysen_zusammenfassen(liste):
    analysen = {}
    result = ""
    for i in liste:
        cell = i["Typ"]
        amount = i["Anzahl"]
        if cell not in analysen:
            analysen[cell] = amount
        else:
            analysen[cell] += amount
    print("Analysenergebnisse:")
    for typ, menge in analysen.items():
        result += f"- {typ}: {menge} Zellen\n"
    return result


print(analysen_zusammenfassen(analysen_liste))
