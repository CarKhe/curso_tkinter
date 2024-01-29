import tkinter as tk

def mensaje():
    print(True)



ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.geometry("600x400")
ventana.iconbitmap("img/ico.ico")

menubutton = tk.Menubutton(ventana,text="archivo")
menubutton.pack()


menu = tk.Menu(menubutton)
menubutton.config(menu=menu)

menu.add_command(label="archivo 1",command=mensaje)
menu.add_command(label="archivo 2")




ventana.mainloop()