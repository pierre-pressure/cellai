def begruessung(name):
    return f"Herzlich Willkommen, {name}!"


user_name = input("Wie lautet dein Name? ")

print(begruessung(user_name))


def analyse_status(anzahl):
    if anzahl >= 20:
        return "Viele Zellen erkannt"
    elif anzahl >= 10:
        return "Mittlere Zellmenge"
    else:
        return "Wenig Zellen erkannt"


try:
    cell_amount = float(input("Bitte gib die Zellanzahl ein: "))
    print(analyse_status(cell_amount))
except ValueError:
    print("Ungültige Eingabe!")
