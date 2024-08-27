import tkinter as tk
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='Important info', message='This is an info message')
    # messagebox.showerror(title='ERROR!!!', message='Something went wrong... :(')
    # messagebox.showwarning(title='WARNING!!!', message='YOU HAVE A VIRUS!!!')

    # answer = messagebox.askyesno(title='Yes or No', message='Do you like pizza?')
    # if answer:
    #     print('Yummy!')
    # else:
    #     print("Why don't you like pizza?")

    # answer = messagebox.askokcancel(title='OK or Cancel', message='Do you want to do something?')
    # if answer:
    #     print('You did it.')
    # else:
    #     print('You cancelled it.')

    # answer = messagebox.askquestion(title='Question', message='Do you like burgers?')

    # if answer == 'yes':
    #     print('I like burgers too!')
    # else:
    #     print('Why not?')

    # answer = messagebox.askretrycancel(title='Retry', message='Do you want to retry?')

    # if answer:
    #     print('You retried successfully!')
    # else:
    #     print('You did not retry')

    answer = messagebox.askyesnocancel(title='Yes, No or Cancel?', message='Do you like coding?')

    if answer == True:
        print('Cool!')
    elif answer == False:
        print('Maybe you should try?')
    else:
        print('You did not answer the question.')



window = tk.Tk()

click_button = tk.Button(window, text='Click me!', command=click)
click_button.pack()

window.mainloop()
