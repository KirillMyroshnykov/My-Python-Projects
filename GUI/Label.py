import tkinter as tk

window = tk.Tk()

photo = tk.PhotoImage(file='D:/PycharmProjects/pythonProject/GUI/images/chiefs.png')

label = tk.Label(window,                     # Window is a master (container for label)
                 text='Forward, Chiefs!',    # Set text that will be added to a label
                 font=('Arial', 20, 'bold'), # Font settings(type, size, appearance)
                 fg='#00FF00',               # Set font color
                 bg='black',                 # Set background color
                 relief="raised",            # Add Border around the label
                 bd=10,                      # Set border size
                 padx=20,                    # Add padding above and under the text on x-axis
                 pady=20,                    # Add padding left and right from the text on y-axis
                 image=photo,                # Add image to a label
                 compound='top')             # Place image above the text

label.pack() # Adds text to a top center of label by default

# label.place(x=100, y=100) -- Add text at given coordinates


window.mainloop()