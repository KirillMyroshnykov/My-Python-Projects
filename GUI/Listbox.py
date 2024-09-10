import tkinter as tk

def submit():
    food = []

    for index in listbox.curselection():        # Submits multiole selection
        food.insert(index, listbox.get(index))

    print('You have ordered:')
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())   # Adjust listbox size

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = tk.Tk()

# Creating listbox
listbox = tk.Listbox(window,
                     bg='#f7ffde',
                     font=('Constantia', 30),
                     width=12,
                     selectmode='multiple')
listbox.pack()

listbox.insert(1,'Pizza')
listbox.insert(2,'Burger')
listbox.insert(3,'French fries')
listbox.insert(4,'Buffalo wings')
listbox.insert(5,'Coca Cola')

listbox.config(height=listbox.size())

# Adding entry
entrybox = tk.Entry(window)
entrybox.pack()

# Adding buttons
submit_button = tk.Button(window, text='Submit', command=submit)
submit_button.pack()

add_button = tk.Button(window, text='Add', command=add)
add_button.pack()

delete_button = tk.Button(window, text='Delete', command=delete)
delete_button.pack()

window.mainloop()