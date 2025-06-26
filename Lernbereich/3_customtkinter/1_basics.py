import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Zellenanalyse")
app.geometry("1280x720")


def begruessung():
    label.configure(text="Willkommen zur Analyse!")


def reset():
    label.configure(text="Analyse zurückgesetzt!")


button = ctk.CTkButton(app, text="Start", command=begruessung)
button.pack(pady=20)

button = ctk.CTkButton(app, text="Zurücksetzen", command=reset)
button.pack(pady=20)

label = ctk.CTkLabel(app, text="Noch keine Analyse gestartet.")
label.pack(pady=10)

app.mainloop()