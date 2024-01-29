import tkinter as tk 

ventana = tk.Tk()
ventana.title("Place")
ventana.iconbitmap("img/ico.ico")

def actualizar_texto(*args):
    etiqueta.config(text=texto.get())
    
    
texto = tk.StringVar(value="Hoal mdo")
texto.set("Nuevo Texto")

entrada = tk.Entry(ventana,textvariable=texto)
entrada.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()
# print(text.get())
# text.set("Holaaaaaa Mundo")
# print(text.get())
texto.trace_add("write",actualizar_texto)

ventana.mainloop() 