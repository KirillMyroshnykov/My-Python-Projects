import tkinter as tk

def submit():
    print(f'The temperature is {scale.get()}°C')

window = tk.Tk()

hot_image = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/hot.png')
hot_label = tk.Label(image=hot_image)
hot_label.pack()

scale = tk.Scale(window,
                 from_=100,             # Top value
                 to=-100,               # Bottom value
                 length=600,            # Scale length
                 orient='vertical',     # Scale orientation
                 tickinterval=10,       # Add numeric indicators for value
                 #showvalue=0,          # Hide current value
                 resolution=5,          # Increment of slider
                 troughcolor='#69EAFF', # Add color to through
                 fg='#FF1C00',          # Font color
                 bg='black')

#scale.set(50)   # Sets cursor at given value
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # Always sets cursor in the middle of scale
scale.pack()

cold_image = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/cold.png')
cold_label = tk.Label(image=cold_image)
cold_label.pack()

button = tk.Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()