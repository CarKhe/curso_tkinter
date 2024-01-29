import tkinter as tk 

ventana = tk.Tk()

imagen = tk.PhotoImage(file="img/luffy.gif")
imagen2 = tk.PhotoImage(file="img/zoro.png")

etiqueta = tk.Label(ventana,image=imagen)
boton = tk.Button(ventana,image=imagen2)

etiqueta.pack()
boton.pack()

ventana.mainloop()