import tkinter as tk 

ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")

texto = tk.Text(ventana)

scrollbar_vertical = tk.Scrollbar(ventana)
scrollbar_vertical.pack(side="right",fill="y")

scrollbar_vertical.config(command=texto.yview)
texto.config(yscrollcommand=scrollbar_vertical.set)
texto.pack(side="left",fill="both",expand=True)

ventana.mainloop()

