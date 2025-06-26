try:
    cell_amount = float(input("Bitte gib die Anzahl der Zellen an: "))
    cell_type = input("Bitte gib den Zellentyp an: ")
    if cell_type.isnumeric():
        print("Das sieht nicht wie ein Zelltyp aus – bitte gib Buchstaben ein.")
    else:
        cell_type = cell_type.lower() # tolerantere eingabe
        match cell_type:
            case "Hefe":
                print("Zelltyp Hefe erkannt")
            case "Erythrozyt":
                print("Zelltyp Erythrozyt erkannt")
            case "Pollen":
                print("Zelltyp Pollen erkannt")
            case _:
                print("Unbekannter Zelltyp")
        print(f"Du hasts {cell_amount} Teilchen des Typs {cell_type} eingegeben")
except ValueError:
    print("Ungültige Eingabe! Stelle sicher, dass nur Zahlen eingegeben wurden.")
