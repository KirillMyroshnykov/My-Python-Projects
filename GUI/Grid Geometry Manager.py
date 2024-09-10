import tkinter as tk

def submit():
    print(first_name_entry.get())
    print(last_name_entry.get())
    print((email_entry.get()))

window = tk.Tk()

info_label = tk.Label(window,
                      text='Enter your Info',
                      font=('Arial', 25),
                      bg='yellow').grid(row=0, column=0, columnspan=2)

first_name_label = tk.Label(window,
                            text='First Name',
                            font=('Arial', 25),
                            bg='red').grid(row=1, column=0)

first_name_entry = tk.Entry(window, font=('Ink Free', 25))
first_name_entry.grid(row=1, column=1)

last_name_label = tk.Label(window,
                           text='Last Name',
                           font=('Arial', 25),
                           bg='green').grid(row=2, column=0)

last_name_entry = tk.Entry(window, font=('Ink Free', 25))
last_name_entry.grid(row=2, column=1)

email_label = tk.Label(window,
                       text='Email',
                       font=('Arial', 25),
                       bg='blue').grid(row=3, column=0)

email_entry = tk.Entry(window, font=('Ink Free', 25))
email_entry.grid(row=3, column=1)

submit_button = tk.Button(window,
                          text='Submit',
                          font=('Arial', 25),
                          command=submit).grid(row=4, column=0, columnspan=2)

window.mainloop()