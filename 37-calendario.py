import os
import tkinter as tk
from tkcalendar import Calendar


def print_date(date):
    print(date)           


ventana = tk.Tk()
ventana.iconbitmap("img/ico.ico")


#cal = Calendar(ventana)
cal = Calendar(ventana,selectmode="day",date_pattern="dd-mm-y")
cal.pack()

cal.bind("<<CalendarSelected>>", lambda e:print_date(cal.get_date()))

ventana.mainloop()

 