import tkinter as tk
from tkinter import filedialog

def openFile():
    path = filedialog.askopenfilename(initialdir='D:\\PycharmProjects\\pythonProject',
                                      title='Open file, okay?',
                                      filetypes=[('text files', '*.txt'),
                                      ('all files', '*.*')])
    file = open(path, 'r')
    print(file.read())
    file.close()

window = tk.Tk()

button = tk.Button(window, text='Open', command=openFile)
button.pack()

window.mainloop()