import os

os.makedirs("OpenCV/Folder", exist_ok=True) # check ob Struktur vorhanden, wenn nicht, erstelle

pfad = os.path.join("OpenCV/Folder", "bericht.txt") # os-unabhängiger Pfad

with open(pfad, "w") as f: # f: file-handler ("Tür" zur Datei, die selbstständig geöffnet werden muss)
    f.write("Analysebericht\nTyp: Hefe\nAnzahl: 12")
