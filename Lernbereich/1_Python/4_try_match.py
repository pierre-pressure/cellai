# „Könnte das hier einen Fehler werfen?“	            → try/except
# „Muss ich Bedingungen prüfen?“	                    → if/elif/else
# „Hab ich klare Werte, auf die ich reagieren will?“	→ match/case

try:
    cell_amount = float(input("Bitte trage die Anzahl der Zellen ein: "))
except ValueError:
    print("Ungültige Eingabe! Bitte trage eine Ganzzahl oder Kommazahl ein..")

typ = input(
    "Bitte gib einen Zelltyp ein: "
)  # input ist immer str, es sei denn es wird konvertiert, also kein try/except notwendig
if typ.isnumeric():
    print("Das sieht nicht wie ein Zelltyp aus – bitte gib Buchstaben ein.")
else:
    match typ:
        case "Hefe":
            print("Hefe erkannt")
        case "Erythrozyt":
            print("Erythrozyt erkannt")
        case "Pollen":
            print("Pollen erkannt")
        case _:
            print("Unbekannter Typ – bitte prüfen")
