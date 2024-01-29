import tkinter as tk 

ventana = tk.Tk()
ventana.geometry("600x400+10+20")
ventana.title("Grid")
ventana.iconbitmap("img/ico.ico")

# label1 = tk.Label(ventana, text="Label 1")
# label1.grid(row=0,column=0,padx=10,pady=10)

# label2 = tk.Label(ventana, text="Label 2")
# label2.grid(row=1,column=0,padx=10,pady=10)

label1 = tk.Label(ventana, text="Label 1,1")
label1.grid(row=0,column=0,padx=5,pady=5)

label2 = tk.Label(ventana, text="Label 1,2")
label2.grid(row=0,column=1,padx=5,pady=5)
label3 = tk.Label(ventana, text="Label 2,1")
label3.grid(row=1,column=0,padx=5,pady=5)

label4 = tk.Label(ventana, text="Label 2,2")
label4.grid(row=1,column=1,padx=5,pady=5)
ventana.mainloop()