import tkinter as tk

food = ['pizza', 'hamburger', 'hotdog']

def order():
    if x.get() == 0:
        print('You ordered a pizza!')
    elif x.get() == 1:
        print('You ordered a hamburger!')
    elif x.get() == 2:
        print('You ordered a hotdog!')
    else:
        print('huh?')

window = tk.Tk()

pizza_image = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/pizza.png')
hamburger_image = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/hamburger.png')
hotdog_image = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/hotdog.png')
food_images = [pizza_image, hamburger_image, hotdog_image]

x = tk.IntVar()

for index in range(len(food)):
    radiobutton = tk.Radiobutton(window,
                                 text=food[index],            # Adds text to radio buttons
                                 variable=x,                  # Groups radio buttons together if they share the same variable
                                 value=index,                 # Assigns each radio button a different value
                                 padx=25,                     # Adds padding on x-axis
                                 font=('Arial', 40, 'bold'),
                                 image= food_images[index],   # Adds image to radio button
                                 compound='left',             # Adds image & text
                                 indicatoron=0,               # Eliminates circle indicators
                                 width=375,                   # Sets width of radio buttons
                                 command=order)               # Sets command of radio button to function

    radiobutton.pack(anchor='w')


window.mainloop()