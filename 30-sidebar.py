import tkinter as tk 

ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")

scrollbar_vertical = tk.Scrollbar(ventana)
scrollbar_vertical.pack(side="right",fill="y")

scrollbar_horizontal = tk.Scrollbar(ventana,orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(fill="x")


ventana.mainloop()


