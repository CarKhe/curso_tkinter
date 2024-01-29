import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw() # oculta ventana principal

#file_path = filedialog.askopenfilename() #askopnfilenames = varios archivos a la vez en una tupla
#print(file_path)


file_obj = filedialog.askopenfile(mode="r")
if file_obj:
    print(file_obj.read())
    file_obj.close()
