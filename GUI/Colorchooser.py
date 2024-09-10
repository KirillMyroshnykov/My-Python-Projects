import tkinter as tk
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor() # Suggests a set of colors
    window.config(bg=color[1])      # Changes background color to the chosen one

window = tk.Tk()
window.geometry('640x480')


button = tk.Button(window, text='Click to add a color', command=click)
button.pack()

window.mainloop()