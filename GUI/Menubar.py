import tkinter as tk
from tkinter import filedialog

def openFile():
    path = filedialog.askopenfilename(initialdir='D:\\PycharmProjects\\pythonProject',
                                      title='Open file, okay?',
                                      filetypes=[
                                          ('text files', '*.txt'),
                                          ('all files', '*.*')
                                      ])
    file = open(path, 'r')
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(initialdir='D:\\PycharmProjects\\pythonProject',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('text file', '*.txt'),
                                        ('all files', '*.*')
                                    ])

    if file is None:        # Thus we have no exception when we interrupt saving a file
        return
    filetext = input('Enter some text I guess: ')   # Adds text to a file from console
    file.write(filetext)
    file.close()

def cut():
    print('You cut the text!') # Printing is here just for simplicity

def copy():
    print('You copied the text!')

def paste():
    print('You pasted the text!')

window = tk.Tk()

menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0, font=('MV Boli', 15)) # Creating File menu at menubar
menubar.add_cascade(label='File', menu=file_menu) # Add cascade named 'File' at menubar
file_menu.add_command(label='Open', command=openFile) # Add command 'Open' inside 'File' cascade
file_menu.add_command(label='Save', command=saveFile) # Add command 'Save' inside 'File' cascade
file_menu.add_separator()
file_menu.add_command(label='Close', command=quit, font=('MV Boli', 15))

edit_menu = tk.Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)

window.mainloop()