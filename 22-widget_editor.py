from tkinter import Tk,Button
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile,asksaveasfile

def abrir_archivo():
    archivo = askopenfile()
    if archivo:
        texto_desplazable.delete(1.0,"end")
        with open(archivo.name, "r") as f:
            texto_desplazable.insert(1.0,f.read())

def guardar_archivo():
    archivo = asksaveasfile()
    if archivo:
        with open(archivo.name,"w") as f:
            f.write(texto_desplazable.get(1.0,"end"))

ventana = Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")

texto_desplazable = ScrolledText(ventana,wrap="word")
texto_desplazable.pack(expand=True, fill="both")

boton_abrir = Button(ventana,text="Abrir", command=abrir_archivo)
boton_abrir.pack(side="left")
boton_guardar = Button(ventana,text="Guardar", command=guardar_archivo)
boton_guardar.pack(side="left")

ventana.mainloop()