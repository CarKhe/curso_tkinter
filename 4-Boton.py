import tkinter as tk
ventana = tk.Tk()

def boton_presionado():
    print("Boton oprimido")
    
def cambiar_texto():
    etiqueta.config(text="El boton cambio el texto")

ventana.title("Mi Boton")
ventana.iconbitmap("img/ico.ico")
boton = tk.Button(ventana,text="Presiona aqui")
boton.config(fg="white",bg="green",font=("Arial",12),command=cambiar_texto)

etiqueta = tk.Label(ventana,text="Hola, soy un label")
etiqueta.pack()
boton.pack()



ventana.mainloop()