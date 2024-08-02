from tkinter import *
from tkinter import messagebox

#Creating Window
window = Tk()
window.title('Window Title')
window.geometry("1280x720+500+20")

#Creating Menu
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
window.config(menu=menubar)

#Creating Workspace
myCanvas = Canvas(window, bg ='blue', height=500, width=500)
pent = myCanvas.create_polygon(100,150, 52,185, 72,240, 129,240, 148,185, fill='lime green')
myCanvas.pack()

#Creating dialog window
userInput = Entry(window)
def dialog():
    messagebox.showinfo('Message Box', userInput.get())
   

myButton = Button(window, text='Click Me', command=dialog)
myButton.pack(padx=20, pady=20)

userInput.pack()

window.mainloop()