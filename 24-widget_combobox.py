import tkinter as tk
from tkinter import ttk

def on_selelccionar(event):
    valor_seleccionado = combobox.get()
    print(f"Se selecciono: {valor_seleccionado}")
    

ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")

combobox = ttk.Combobox(ventana,width=30,font=("Arial",12),foreground="blue",background="white")
combobox.pack()

elementos = ["E1","E2","E3"]
elementos.remove("E2")
indice = 1
nuevo_valor = "Elemento cambiado"
elementos[indice] = nuevo_valor
combobox["values"] = elementos

combobox.bind("<<ComboboxSelected>>",on_selelccionar)

ventana.mainloop()