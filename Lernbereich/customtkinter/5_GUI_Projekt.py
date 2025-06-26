import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

analysen = []

app = ctk.CTk()
app.title("Zelltyp + Anzahl eingeben & speichern")
app.geometry("720x480")

frame_eingabe = ctk.CTkFrame(app) # frame ist wie divs: container
frame_eingabe.pack(pady=10)

entry_cell = ctk.CTkEntry(frame_eingabe, placeholder_text="Zelltyp", width=200)
entry_cell.pack(pady=5)

entry_amount = ctk.CTkEntry(frame_eingabe, placeholder_text="Anzahl", width=200)
entry_amount.pack(pady=5)

dropdown_typen = ctk.CTkOptionMenu(
    frame_eingabe, values=["Keine Einträge vorhanden"], width=200
)
dropdown_typen.set("Zelltyp-Auswahl")
dropdown_typen.pack(pady=5)

textbox = ctk.CTkTextbox(app, width=500, height=150)
textbox.pack(pady=10)

frame_buttons = ctk.CTkFrame(app, fg_color="#3b3b3b", corner_radius=10)
frame_buttons.pack(pady=10)


def speichere_analyse():
    user_input = ""
    multiple = ""
    cells = entry_cell.get()
    try:
        amount = int(entry_amount.get())
        if amount > 1:
            multiple = "n"
        user_input = f"Gespeichert: {cells} – Anzahl: {amount} Zelle{multiple}"
        analysen.append({"Typ": cells, "Anzahl": amount})
        textbox.delete("0.0", "end")
        textbox.insert("0.0", user_input)
        entry_cell.delete(0, "end")
        entry_amount.delete(0, "end")
        aktualisiere_dropdown()
    except ValueError:
        textbox.delete("0.0", "end")
        textbox.insert("0.0", "Ungültige Eingabe! Bitte eine Zahl eingeben.")
    aktualisiere_status()


def zeige_alle():
    empty = "Keine Einträge vorhanden"
    textbox.delete("0.0", "end")
    if analysen == []:
        textbox.insert("0.0", empty)
    else:
        liste = ""
        for eintrag in analysen:
            zellen = eintrag["Typ"].lower().capitalize()
            menge = eintrag["Anzahl"]
            liste += f"- {zellen}: {menge} Zellen \n"
        text_output = f"Gespeicherte Analysen: \n{liste}"
        textbox.insert("0.0", text_output)


def reset_analysieren():
    analysen.clear()
    textbox.delete("0.0", "end")
    aktualisiere_status()


def aktualisiere_dropdown():
    typen_liste = list(
        set(eintrag["Typ"] for eintrag in analysen)
    )  # set entfernt doppelte Einträge
    if typen_liste:
        dropdown_typen.configure(values=typen_liste)
    else:
        dropdown_typen.configure(values="Keine Einträge vorhanden")


def zeige_auswahl():
    auswahl = dropdown_typen.get()
    gesamt = 0
    treffer = 0
    for eintrag in analysen:
        if eintrag["Typ"] == auswahl:
            gesamt += eintrag["Anzahl"]
            treffer += 1
    textbox.delete("0.0", "end")
    if treffer == 0:
        textbox.insert("0.0", "Keine passenden Einträge gefunden.")
    else:
        textbox.insert(
            "0.0", f"{auswahl} – Gesamt: {gesamt} Zellen\n({treffer} Einträge)"
        )


def aktualisiere_status():
    eintraege = len(analysen)
    zellen_gesamt = sum(e["Anzahl"] for e in analysen)
    text = f"{eintraege} Einträge – {zellen_gesamt} Zellen insgesamt"
    if zellen_gesamt >= 1:
        text_color = "green"
        text_output = f"{eintraege} Einträge – {zellen_gesamt} Zellen insgesamt"
    else:
        text_color = "red"
        text_output = "Keine Einträge – noch keine Analyse durchgeführt."
    status_label.configure(text=text_output, text_color=text_color, font=("Arial", 12))


button_save = ctk.CTkButton(frame_buttons, text="Speichern", command=speichere_analyse)
button_save.pack(side="left", padx=10)

button_reset = ctk.CTkButton(
    frame_buttons, text="Zurücksetzen", command=reset_analysieren
)
button_reset.pack(side="left", padx=10)

button_dd = ctk.CTkButton(frame_buttons, text="Typ anzeigen", command=zeige_auswahl)
button_dd.pack(side="left", padx=10)

button_show = ctk.CTkButton(frame_buttons, text="Alle anzeigen", command=zeige_alle)
button_show.pack(side="left", padx=10)

status_label = ctk.CTkLabel(app, text="Noch keine Analyse durchgeführt.", anchor="w")
status_label.configure(text_color="red", font=("Arial", 12))
status_label.pack(fill="x", padx=10, pady=(5, 10))

app.mainloop()
