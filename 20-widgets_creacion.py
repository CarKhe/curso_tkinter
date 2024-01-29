import tkinter as tk
from tkinter.scrolledtext import ScrolledText



ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")


texto = tk.Text(ventana, width=40,height=10,wrap="word",bg="lightgray",fg="black", padx=10,pady=10, font=("Arial",12))
texto.insert("1.0","Mensaje enviado nose que poner alch we")
# resaltado = es a la etiqueta que se le da al texto para ponerle otros atributos
texto.insert("end","\notro mensaje de no se que ponera aqui","resaltado")
texto.tag_configure("resaltado",background="orange", foreground="black")
texto.pack()

contenido = texto.get("1.0","end")
texto.delete("1.0","end")
print(contenido)
texto_desplazable = ScrolledText(ventana, width=20,height=4,wrap="word",bg="lightgray",fg="black", padx=10,pady=10, font=("Arial",12))
texto_desplazable.pack()


ventana.mainloop()