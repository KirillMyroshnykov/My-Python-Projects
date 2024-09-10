import tkinter as tk
import time

WIDTH = 500
HEIGHT = 354
xVelocity = 3
yVelocity = 3

window = tk.Tk()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = tk.PhotoImage(file='D:\\PycharmProjects\\pythonProject\\GUI\\images\\space.png')
background = canvas.create_image(0,0, image=background_image, anchor=tk.NW)

ufo_image = tk.PhotoImage(file='D:\\PycharmProjects\\pythonProject\\GUI\\images\\ufo.png')
my_image = canvas.create_image(0,0, image=ufo_image, anchor=tk.NW)

ufo_width = ufo_image.width()
ufo_height = ufo_image.height()

while True:
    coordinates = canvas.coords(my_image)

    if coordinates[0] >= (WIDTH-ufo_width) or coordinates[0] < 0:
        xVelocity = -xVelocity

    if coordinates[1] >= (HEIGHT-ufo_height) or coordinates[1] < 0:
        yVelocity = -yVelocity

    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()