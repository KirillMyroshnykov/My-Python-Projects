import tkinter as tk
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='D:\\PycharmProjects\\pythonProject',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All files', '.*')
                                    ])

    if file is None:        # Thus we have no exception when we interrupt saving a file
        return
    #filetext = str(text.get('1.0', 'end'))         # Adds text to a file from text area
    filetext = input('Enter some text I guess: ')   # Adds text to a file from console
    file.write(filetext)
    file.close()


window = tk.Tk()

text = tk.Text()
text.pack()

button = tk.Button(window, text='Save', command=saveFile)
button.pack()

window.mainloop()