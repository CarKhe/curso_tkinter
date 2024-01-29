import tkinter as tk

def copiar():
   texto.event_generate("<<Copy>>") 

def cortar():
   texto.event_generate("<<Cut>>") 
    
def pegar():
   texto.event_generate("<<Paste>>") 
    




ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("img/ico.ico")


texto = tk.Text(ventana)
texto.pack()

btn_copiar = tk.Button(ventana,text="Copiar",command=copiar)
btn_copiar.pack()
btn_cortar = tk.Button(ventana,text="Cortar",command=cortar)
btn_cortar.pack()
btn_pegar = tk.Button(ventana,text="Pegar",command=pegar)
btn_pegar.pack()



ventana.mainloop()