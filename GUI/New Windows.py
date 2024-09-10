import tkinter as tk

def create_window():
    #new_window = tk.Toplevel() # TopLevel = new window 'on top' of other windows, linked to a bottom window
    new_window = tk.Tk()        # Tk() = new independent window
    old_window.destroy()        # Close out of old window

old_window = tk.Tk()

tk.Button(old_window, text='Create new window', command=create_window).pack()

old_window.mainloop()