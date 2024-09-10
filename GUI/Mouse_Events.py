import tkinter as tk

def doSomething(event):
    print('Mouse coordinates: ' + str(event.x) +','+ str(event.y))

window = tk.Tk()

# window.bind('<Button-1>', doSomething) # Left mouse button click event
# window.bind('<Button-2>', doSomething) # Scroll wheel click event
# window.bind('<Button-3>', doSomething) # Right mouse button click event
# window.bind('<ButtonRelease>', doSomething) # Event occurs when mouse button is released
# window.bind('<Leave>', doSomething) # Event occurs when the cursor leaves the window
# window.bind('<Enter>', doSomething) # Event occurs when the cursor entered the window
# window.bind('<Motion>', doSomething) # Event occurs while the cursor is moving inside the window


window.mainloop()