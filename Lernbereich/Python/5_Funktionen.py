def begrüßung():
    print("Willkommen zur Analyse!")


begrüßung()


def zellen_melden(anzahl, typ):
    print(f"Erkannte Zellen: {anzahl}")
    print(f"Zelltyp: {typ}")


zellen_melden(12.5, "Hefe")


def zellmenge_doppeln(anzahl):
    anzahl_d = anzahl * 2
    return anzahl_d


print(f"Die neue Anzahl beträgt: {zellmenge_doppeln(5)}")
