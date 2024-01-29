import tkinter as tk 

ventana = tk.Tk()
ventana.title("Pack")
ventana.iconbitmap("img/ico.ico")

frame_button = tk.Frame(ventana)
frame_button.pack(pady=10)

btn_1 = tk.Button(frame_button,text="Boton 1")
btn_1.pack(side="right",padx=5)
btn_2 = tk.Button(frame_button,text="Boton 2")
btn_2.pack(side="left",padx=5)
btn_3 = tk.Button(frame_button,text="Boton 3")
btn_3.pack(padx=5)


# label1 = tk.Label(ventana, text="Label 1")
# label1.pack(side="left",padx=5)

# label2 = tk.Label(ventana, text="Label 2")
# label2.pack(side="left",padx=5)

ventana.mainloop() 