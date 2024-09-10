import tkinter as tk

def showKey(event):
    label.config(text=event.keysym)

window = tk.Tk()

label = tk.Label(window, font=('Helvetica', 100))
label.pack()

window.bind('<Key>', showKey)

window.mainloop()