import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw() # oculta ventana principal

#file_path = filedialog.askopenfilename() #askopnfilenames = varios archivos a la vez en una tupla
#print(file_path)


file_obj = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
if file_obj:
    file_obj.write("Hola Archivo")
    file_obj.close()
