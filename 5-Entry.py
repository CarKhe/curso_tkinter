import tkinter as tk
ventana = tk.Tk()

def aplicar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)


ventana.title("Mi Entry")
ventana.geometry("200x100")
ventana.resizable(False,False)
ventana.iconbitmap("img/ico.ico")


etiqueta = tk.Label(ventana,text="Abajo hay una entrada")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.config(fg="blue",bg="lightgray",font=("Arial",12))
entrada.insert(0,"Default text")
entrada.pack()

boton = tk.Button(ventana, text="Aplicar Texto",command=aplicar_texto)
boton.pack()

ventana.mainloop()