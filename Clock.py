import tkinter as tk
import time

def update():
    time_string = time.strftime('%H:%M:%S')
    time_label.config(text=time_string)

    day_string = time.strftime('%A')
    day_label.config(text=day_string)

    date_string = time.strftime('%B %d, %Y')
    date_label.config(text=date_string)

    window.after(1000, update)  # Updates time label every second


window = tk.Tk()
window.geometry('500x500')

time_label = tk.Label(window, font=('Arial', 50), fg='#00FF00', bg='black', width=500)
time_label.pack()

day_label = tk.Label(window, font=('Ink Free', 40))
day_label.pack()

date_label = tk.Label(window, font=('Ink Free', 40))
date_label.pack()

update()

window.mainloop()