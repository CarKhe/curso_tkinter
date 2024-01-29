import tkinter as tk 

ventana = tk.Tk()
ventana.title("Int")
ventana.iconbitmap("img/ico.ico")
booleano = tk.BooleanVar(value=True)

def actualizar(*args):
    print(booleano.get())

casilla = tk.Checkbutton(ventana, text="Aceptar", variable=booleano)
casilla.pack()

booleano.trace_add("write",actualizar)

ventana.mainloop() 