import tkinter as tk 

ventana = tk.Tk()
ventana.title("Place")
ventana.iconbitmap("img/ico.ico")

# label1 = tk.Label(ventana, text="Label 1")
# label1.place(x=50,y=50)

# label2 = tk.Label(ventana, text="Label 2")
# label2.place(x=100,y=100)


label1 = tk.Label(ventana, text="Label 1")
label1.place(relx=0.25,rely=0.25)

label2 = tk.Label(ventana, text="Label 2")
label2.place(relx=0.5,rely=0.5)

label3 = tk.Label(ventana, text="Label 3")
label3.place(relx=0.75,rely=0.75)

label4 = tk.Label(ventana, text="Label 4")
label4.place(relx=0.99,rely=0.99)

ventana.mainloop() 