import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login to D&D Roller")
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

# checkbox = ctk.CTkCheckBox(master=frame, text="Remember me")
# checkbox.pack(pady=12, padx=10)

root.mainloop()







# ventana = tk.Tk()
# ventana.geometry("300x300")
# ventana.withdraw()
#
# etiqueta = tk.Label(ventana, text = "Hola Mundo")
# # etiqueta.pack(side = "tkinter.BOTTOM") # colocar la etiqueta en el fondo
# # etiqueta.pack(fill = tk.X) # para que ocupe toda la línea
# # etiqueta.pack(fill = tk.Y, expand = True) # colocarla en el centro verticalmente
# # etiqueta.pack(fill = tk.BOTH, expand = true) # colocarla en el central verticalmente Y horizontalmente
#
# # boton1 = tk.BUTTON(ventana, text = "Presiona este botón")
# # boton1.pack()
#
# var = tk.StringVar(ventana)
# var.set(None)
# elección_del_usuario = var.get()
# print(elección)
#
#
# ventana.mainloop()

