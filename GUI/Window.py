import tkinter as tk
window = tk.Tk() # Instantiate an instance of a window

window.geometry('640x480') # Set window size

window.title('First GUI program') # Set window title

icon = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/football.png') # Instantiate an image

window.iconphoto(True, icon) # Replace an icon at window

window.config(background='black') # Set any changes you wish to the window
                                  # (About colors: you can use hexadecimal of the color)


window.mainloop() # Place window on computer screen