import tkinter as tk


def on_seleccionar(event):
    indice = listbox.curselection()
    elemento = listbox.get(indice)
    print(f"Indice: {elemento}, seleccioando")
    
def unclick(event):
    print("Se dio un click en el listbox")

def doble_click(event):
    print("Se dio doble click en el listbox")


ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")


#listbox = tk.Listbox(ventana, width=30,height=10, font=("Arial",12),fg="blue",bg="black",selectmode=tk.MULTIPLE)
listbox = tk.Listbox(ventana, width=30,height=10, font=("Arial",12),fg="blue",bg="black")

listbox.insert(0,"elemento 0")
listbox.insert(tk.END,"elemento 1")
listbox.insert(tk.END,"elemento 2")
listbox.insert(3,"elemento 3")
listbox.delete(3)
listbox.pack()

listbox.bind("<<ListboxSelect>>", on_seleccionar)
listbox.bind("<Button-1>", unclick)
listbox.bind("<Double Button-1>", doble_click)


ventana.mainloop()