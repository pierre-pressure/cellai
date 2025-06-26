import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Zellenanalyse")
app.geometry("1280x720")

entry = ctk.CTkEntry(app, placeholder_text="Zelltyp eingeben")
entry.pack(pady=10)

label = ctk.CTkLabel(app, text="Noch nichts eingegeben.")
label.pack(pady=10)


def analysieren():
    inhalt = entry.get()
    if inhalt:
        label.configure(text=f"Analyse gestartet für: {inhalt}")
    else:
        label.configure(text="Bitte Zelltyp eingeben!")


button = ctk.CTkButton(app, text="Analyse starten", command=analysieren)
button.pack(pady=(100,1))

app.mainloop()
