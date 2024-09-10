import tkinter as tk

def display():
    if x.get():
        print('You agreed! :)')
    else:
        print('You disagreed :(')

window = tk.Tk()

x = tk.BooleanVar() # Holds boolean type of variants

python_image = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/python.png')

checkbox = tk.Checkbutton(window,
                          text='Do you agree?',
                          variable=x,          # Groups checkboxes together if they share the same variable
                          onvalue=True,        # Value stored inside the variable when checkbox is toggled on
                          offvalue=False,      # Value stored inside the variable when checkbox is toggled off
                          font=('Comic Sans', 20),
                          fg='#00FF00',
                          bg='black',
                          activeforeground='#00FF00',
                          activebackground='black',
                          padx=25,
                          pady=10,
                          image=python_image,
                          compound='left',
                          command=display)

checkbox.pack()

window.mainloop()