import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archvio de texto", "*.txt"),("Todos los archivos", "*.*")])
    if file_path:
        with open(file_path,"r") as file_obj:
            contenido = file_obj.read()
            text_widget.delete(1.0,tk.END)
            text_widget.insert(tk.INSERT,contenido)
            
def guardar_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archvio de texto", "*.txt"),("Todos los archivos", "*.*")])
    if file_path:
        with open(file_path,"w") as file_obj:
            contenido = text_widget.get(1.0,tk.END)
            file_obj.write(contenido)

ventana = tk.Tk()
ventana.iconbitmap("img/ico.ico")

#file_path = filedialog.askopenfilename() #askopnfilenames = varios archivos a la vez en una tupla
#print(file_path)

text_widget = tk.Text(ventana,wrap="word")
text_widget.pack(expand=True,fill="both")

abrir_boton = tk.Button(ventana,text="Abrir Archivo", command=abrir_archivo)
guardar_boton = tk.Button(ventana,text="Guardar Archivo", command=guardar_archivo)
abrir_boton.pack(side="left")
guardar_boton.pack(side="right")


ventana.mainloop()

