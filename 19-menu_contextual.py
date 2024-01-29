import tkinter as tk

def mostrar_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root,event.y_root)

ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.geometry("600x400")
ventana.iconbitmap("img/ico.ico")


menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label="Copiar")
menu_contextual.add_command(label="Pegar")


entrada = tk.Entry(ventana)
entrada.pack()

entrada.bind("<Button-3>",mostrar_menu_contextual)
#ventana.bind("<Button-3>",mostrar_menu_contextual)
ventana.mainloop()