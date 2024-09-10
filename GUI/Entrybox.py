import tkinter as tk

def submit():
    username = entrybox.get() # Returns input as a string
    print(f'Hello {username}')
    entrybox.config(state='disabled') # After submitting, entrybox is disabled

def delete():
    entrybox.delete(0, 'end') # Two arguments: first and last character

def backspace():
    entrybox.delete(len(entrybox.get())-1, 'end')

window = tk.Tk()

# ENTRYBOX CONSTRUCTOR
entrybox = tk.Entry(window,
                    font=('Arial', 40,),
                    fg='#00FF00',
                    bg='black',
                    show='*')                   # Display * instead of letters

#entrybox.insert(0, 'Log in') #Add default text
entrybox.pack(side='left') # Adding an entrybox

submit_button = tk.Button(window, text='Submit', command=submit)
submit_button.pack(side='right') # Adding a submit button

delete_button = tk.Button(window, text='Delete', command=delete)
delete_button.pack(side='right') # Adding a delete button

backspace_button = tk.Button(window, text='Backspace', command=backspace)
backspace_button.pack(side='right') # Adding a backspace button

window.mainloop()