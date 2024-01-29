import tkinter as tk 

ventana = tk.Tk()
ventana.title("Int")
ventana.iconbitmap("img/ico.ico")


def actualizar(*args):
    print(entero.get())

entero = tk.IntVar(value=123)
print(entero.get())

opcion1 = tk.Radiobutton(ventana,text="valor 1", variable=entero,value=1)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana,text="valor 2", variable=entero,value=2)
opcion2.pack()

entero.trace_add("write",actualizar)

ventana.mainloop() 