import tkinter as tk

def send():
    user_input = text.get('1.0', 'end')
    print(user_input)

window = tk.Tk()

text = tk.Text(window,
               bg='light yellow',
               font=('Ink Free', 25),
               height=10,
               width=60,
               padx=20,     # Indentation from ceiling
               pady=20,     # Indentation from side
               fg='red')
text.pack()

send_button = tk.Button(window, text='Send', command=send)
send_button.pack()

window.mainloop()