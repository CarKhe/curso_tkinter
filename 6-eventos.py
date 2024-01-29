import tkinter as tk

def on_click(event):
    print(f"Btn {event.widget['text']} presionado")
    
    
    
def on_key_press(event):
    if event.char == "a":
        print("tecla a presionada")

def on_resize(event):
    print(f"La ventana fue redimenzionada a {event.width}x{event.height} y dimensiones de {event.x}x{event.y} dimension")


def on_mouse_move(event):
    print(f"Mouse movido en {event.x},{event.y} ")
    
    
    
    
ventana = tk.Tk()

buttons = [tk.Button(ventana,text=f"Boton {i}") for i in range(3)]
for button in buttons:
    button.pack()
    button.bind("<Button-1>",on_click)
    
#button = tk.Button(ventana, text = "haz click aqui")
#button.pack()

#button-1 = click izquierdo del mouse
#button-2 = click del scroll del mouse
#button-3 = click derecho del mouse

#button.bind("<Button-1>",on_click)
#ventana.bind("<KeyPress>",on_key_press)
#
# ventana.bind("<Configure>",on_resize)
#ventana.bind("<Motion>",on_mouse_move)


ventana.mainloop()