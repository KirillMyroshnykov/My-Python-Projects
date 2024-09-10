import tkinter as tk
from Ball import *
import time

WIDTH = 500
HEIGHT = 500

window = tk.Tk()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

tennis_ball = Ball(canvas, 0,0, 15,6, 4, 'green')
volley_ball = Ball(canvas, 0,0, 40, 3, 4, 'white')
basket_ball = Ball(canvas, 0,0, 80, 3, 2, 'orange')
ping_pong = Ball(canvas, 0,0, 10, 7, 5, 'blue')
football = Ball(canvas, 0,0, 50, 4, 5, 'brown')

while True:
    tennis_ball.move()
    volley_ball.move()
    basket_ball.move()
    ping_pong.move()
    football.move()
    window.update()
    time.sleep(0.01)

window.mainloop()