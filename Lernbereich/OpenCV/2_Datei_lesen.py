import os

pfad = os.path.join("OpenCV/Folder", "bericht.txt")

with open(pfad, "r") as f:
    content = f.read().splitlines() # splitlines() erstellt pro Zeile eine Liste, kein dict.

print(content)