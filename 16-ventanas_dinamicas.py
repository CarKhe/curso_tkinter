import tkinter as tk
#variable tkinter
ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.geometry("600x400")
ventana.iconbitmap("img/ico.ico")



def cerrar_toplevel(ventana):
    ventana.destroy()


def agregar_ventana():
    vetnana_toplevel = tk.Toplevel(ventana)
    vetnana_toplevel.title("Ventana toplevel")
    vetnana_toplevel.geometry("400x200")


vetnana_toplevel = tk.Toplevel(ventana)
vetnana_toplevel.title("Ventana toplevel")
vetnana_toplevel.geometry("400x200") 

boton = tk.Button(ventana,text="Agregar ventana",command=agregar_ventana)
boton_cerrar = tk.Button(ventana,text="Cerrar ventana",command= lambda :cerrar_toplevel(vetnana_toplevel))
boton.pack()
boton_cerrar.pack()




ventana.mainloop()