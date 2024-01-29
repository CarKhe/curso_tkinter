import tkinter as tk 



ventana = tk.Tk()
canvas = tk.Canvas(ventana,width=500,height=300,bg="lightblue")
#posicionx,posiciony,ancho,alto
rectangulo = canvas.create_rectangle(50,50,150,100,fill="green",outline="black",width=2)
canvas.create_oval(200,50,300,150,fill="blue", outline="purple",width=2)
canvas.create_polygon(350,50,400,100,350,150,fill="purple",outline="black",width=3)
canvas.create_line(10,200,100,200)
canvas.create_line(10,250,200,250, fill="orange",width=5,dash=(5,2),capstyle="round")
#canvas.move(rectangulo,100,100)
canvas.pack()





ventana.mainloop()