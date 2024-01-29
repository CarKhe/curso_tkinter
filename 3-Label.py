import time
import tkinter as tk
ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.iconbitmap("img/ico.ico")
ventana.configure(bg="lightblue")

etiqueta = tk.Label(ventana,text="Ejemplo Label")
etiqueta.config(fg="blue",bg="yellow",font=("Arial",32,"bold"))
etiqueta.config(text="Nuevo texto")
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    #atributo que se puede utilizar despues de tiempo designado
    ventana.after(1000,actualizar_hora)

actualizar_hora()
ventana.mainloop()