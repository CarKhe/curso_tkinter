import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archvio de texto", "*.txt"),("Todos los archivos", "*.*")])
    if file_path:
        with open(file_path,"r") as file_obj:
            contenido = file_obj.read()
            text_widget.delete(1.0,tk.END)
            text_widget.insert(tk.INSERT,contenido)

ventana = tk.Tk()
ventana.iconbitmap("img/ico.ico")

#file_path = filedialog.askopenfilename() #askopnfilenames = varios archivos a la vez en una tupla
#print(file_path)

text_widget = tk.Text(ventana,wrap="word")
text_widget.pack(expand=True,fill="both")

abrir_boton = tk.Button(ventana,text="Abrir Archivo", command=abrir_archivo)
abrir_boton.pack()

ventana.mainloop()

