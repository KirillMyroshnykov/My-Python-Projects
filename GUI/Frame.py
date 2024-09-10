import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window, bg='pink', bd=5, relief=tk.SUNKEN)
frame.pack()

# Creating WASD buttons
tk.Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=tk.TOP)
tk.Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=tk.LEFT)
tk.Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=tk.LEFT)
tk.Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=tk.LEFT)

window.mainloop()