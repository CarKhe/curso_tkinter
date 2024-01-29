import tkinter as tk 

ventana = tk.Tk()
ventana.title("Int")
ventana.iconbitmap("img/ico.ico")

decimal = tk.DoubleVar(value=12.4)

control_deslizante = tk.Scale(ventana,variable=decimal,from_ =0,to=50,resolution=0.1, orient="horizontal")
control_deslizante.pack()

ventana.mainloop() 