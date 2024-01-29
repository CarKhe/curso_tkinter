import tkinter as tk 
from PIL import Image,ImageTk


ventana = tk.Tk()
etiqueta = tk.Label(ventana)
etiqueta.pack()

imagen_pil = Image.open("img/nami.jpg").resize((50,50)).rotate(45)
imagen_tk = ImageTk.PhotoImage(imagen_pil)

boton = tk.Button(ventana,image=imagen_tk)
boton.pack()


ventana.mainloop()