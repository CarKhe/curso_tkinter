import tkinter as tk
ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("600x400")
ventana.iconbitmap("img/ico.ico")
ventana.configure(bg="lightblue")
frame1 = tk.Frame(ventana)
#bd = borde 
frame1.configure(width=300,height=200,bg="red",bd=5)
frame2 = tk.Frame(frame1)
frame2.configure(width=100,height=100,bg="purple",bd=5)

btn = tk.Button(frame1,text="Hola")
#pad = padding
label_frame = tk.LabelFrame(ventana,text="Grupo de widgets",bg="yellow", padx=10,pady=10)
label_frame.configure(width=300,height=200)




label_frame.pack()
frame1.pack()
frame2.pack()
btn.pack()
ventana.mainloop()