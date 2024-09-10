import tkinter as tk
from tkinter import ttk

window = tk.Tk()

notebook = ttk.Notebook(window) # Widget that manages a collection of windows/displays

tab1 = tk.Frame(notebook) # New frame for tab 1
tab2 = tk.Frame(notebook) # New frame for tab 2

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand=True, fill='both') # expand = expand to fill any space not otherwise used
                                        # fill = fill space on x and y axis

tk.Label(tab1, text='Hello, this is Tab#1', width=50, height=25).pack()
tk.Label(tab2, text='Hello, this is Tab#2', width=50, height=25).pack()

window.mainloop()