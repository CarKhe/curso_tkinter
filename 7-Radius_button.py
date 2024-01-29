import tkinter as tk 

ventana = tk.Tk()
ventana.geometry("600x400+10+20")

def mostrar_seleccion():
    if variable_control.get() != 0:
        print("Opcion Seleccionada", variable_control.get())
    else:
        print("ningun valor", False)
        
def cambiar_color_ventana():
    variable = variable_control.get()
    if variable == 1:
        ventana.config(bg="red")
    elif variable == 2:
        ventana.config(bg="purple")
    else:
        print("No hay seleccion")
    
    
#option1 = tk.Radiobutton(ventana,text="Opcion 1")
#option1 = tk.Radiobutton(ventana,text="Opcion 1", font=("Arial", 14), fg="blue", bg="lightgray")
#option1.pack()

variable_control = tk.IntVar()
option1 = tk.Radiobutton(ventana,text="Opcion 1", font=("Arial", 14), variable= variable_control, value=1, command=cambiar_color_ventana)
option2 = tk.Radiobutton(ventana,text="Opcion 2", font=("Arial", 14), variable= variable_control, value=2, command=cambiar_color_ventana)


boton = tk.Button(ventana,text="Mostrar seleccion",command=mostrar_seleccion)


option1.pack()
option2.pack()
boton.pack()
ventana.mainloop()