import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.geometry("600x400")
ventana.iconbitmap("img/ico.ico")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo",menu=archivo_menu)

archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar")

editar_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Editar",menu=editar_menu)
editar_menu.add_command(label="Deshacer")
editar_menu.add_command(label="Rehacer")


ventana.mainloop()