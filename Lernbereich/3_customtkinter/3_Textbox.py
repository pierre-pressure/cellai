import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Analysebericht")
app.geometry("500x400")


textbox = ctk.CTkTextbox(app, width=400, height=200)
textbox.pack(pady=20)


def zeige_ergebnis():
    ergebnis = "Analyseergebnisse:\n- Hefe: 12 Zellen\n- Pollen: 5 Zellen"
    textbox.delete("0.0", "end")
    textbox.insert("0.0", ergebnis)


def textbox_leeren():
    textbox.delete("0.0", "end")


button = ctk.CTkButton(app, text="Ergebnisse anzeigen", command=zeige_ergebnis)
button.pack(pady=10)

button_del = ctk.CTkButton(app, text="Ergebnisse löschen", command=textbox_leeren)
button_del.pack(pady=10)

app.mainloop()
