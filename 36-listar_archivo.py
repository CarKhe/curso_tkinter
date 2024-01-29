import os
import tkinter as tk
from tkinter import filedialog

def seleccionar_directorio():
    dir_path = filedialog.askdirectory()
    if dir_path:
        listabox.delete(0,tk.END)
        for file in os.listdir(dir_path):
            listabox.insert(tk.END,file)
            


ventana = tk.Tk()
ventana.iconbitmap("img/ico.ico")


listabox = tk.Listbox(ventana)
listabox.pack(expand=True,fill="both")

seleccionar_boton = tk.Button(ventana,text="Seleccionar Directorio",command=seleccionar_directorio)
seleccionar_boton.pack()


ventana.mainloop()

