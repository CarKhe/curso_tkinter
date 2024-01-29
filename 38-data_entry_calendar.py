
import tkinter as tk
from tkcalendar import DateEntry


def print_date(date):
    print(date)           


ventana = tk.Tk()
ventana.iconbitmap("img/ico.ico")

data_entry = DateEntry(ventana,selectmode="day",date_pattern="dd-mm-y")
data_entry.pack() 

ventana.mainloop()

 