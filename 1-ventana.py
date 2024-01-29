import tkinter as tk
#variable tkinter
ventana = tk.Tk()

ventana.title("Mi primera Ventana")
#tamaño de la ventana mas las cordenadas en pantalla
ventana.geometry("600x400+10+20")
ventana.minsize(400,200)
ventana.maxsize(800,600)
ventana.iconbitmap("img/ico.ico")
#python-tkinter-colores
ventana.configure(bg="lightblue")
#bloqueo el tamaño de la ventana (Horizontal, Vertical)
ventana.resizable(False,False)
#opacidad
ventana.attributes("-alpha",0.8)
#abrir la ventana
ventana.mainloop()