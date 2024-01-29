import tkinter as tk 

ventana = tk.Tk()
ventana.geometry("600x400+10+20")
ventana.title("ejemplo Grid")
ventana.iconbitmap("img/ico.ico")

def on_check_button():
    print("Variable seleccioando: ")

def habilitar_boton():
    if variable_check_1.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

variable_check_1 = tk.BooleanVar()
#variable_check_2 = tk.BooleanVar()

#check2 = tk.Checkbutton(ventana,text="Check 2",variable=variable_check_2, command= habilitar_boton) 
check1 = tk.Checkbutton(ventana,text="Check 1",variable=variable_check_1, command= habilitar_boton) 

boton = tk.Button(ventana,text="Boton", state="disabled")

check1.pack()
#check2.pack()
boton.pack()
ventana.mainloop()