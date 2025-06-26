import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

analysen = [
    {"Typ": "Hefe", "Anzahl": 5},
    {"Typ": "Pollen", "Anzahl": 12},
    {"Typ": "Erythrozyt", "Anzahl": 2},
    {"Typ": "Hefe", "Anzahl": 13},
]


app = ctk.CTk()
app.title("Zelltyp-Suche")
app.geometry("600x400")

entry = ctk.CTkEntry(app, placeholder_text="Zelltyp eingeben")
entry.pack(pady=10)

textbox = ctk.CTkTextbox(app, width=500, height=150)
textbox.pack(pady=10)


def suche_zelltyp():
    content = entry.get()
    result = ""
    for eintrag in analysen:
        if eintrag["Typ"].lower().capitalize() == content.lower().capitalize():
            result += f'Typ: {eintrag["Typ"]} – Anzahl: {eintrag["Anzahl"]} Zellen \n'
    if result == "":
        result = "Zelltyp nicht gefunden!"
    textbox.delete("0.0", "end")
    textbox.insert("0.0", result)


def suche_del():
    textbox.delete("0.0", "end")


button_search = ctk.CTkButton(app, text="Suchen", command=suche_zelltyp)
button_search.pack(pady=10)

button_del = ctk.CTkButton(app, text="Suche löschen", command=suche_del)
button_del.pack(pady=10)

app.mainloop()
