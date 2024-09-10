import tkinter as tk

count = 0
def click():
    global count
    count += 1
    print(count)

window = tk.Tk()

picture = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/like.png')

button = tk.Button(window,                      # Set master(container for button)
                   text='Click Me!',            # Add text on the button
                   command=click,               # Performs button's callback
                   font=('Comic Sans', 30,),    # Font settings
                   fg='#00FF00',                # Font color
                   bg='black',                  # Background color
                   activeforeground='#00FF00',
                   activebackground='black',    # Thus button no flashes anymore while clicking
                   state='active',              # 'disable' option disables clicking
                   image=picture,               # Add an image
                   compound='bottom')           # Place image above the text

button.pack()
window.mainloop()