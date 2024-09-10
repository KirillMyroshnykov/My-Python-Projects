import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, height=500, width=500)
canvas.pack()

#CREATING LINE
#blue_line = canvas.create_line(0,0, 500,500, fill='blue', width=5)
#red_line = canvas.create_line(0,500, 500,0, fill='red', width=5)

#CREATING RECTANGLE
#canvas.create_rectangle(50,50, 250,250, fill='red')

#CREATING TRIANGLE
#canvas.create_polygon(250,0, 0,500, 500,500, fill='yellow', width=5)

#CREATING CIRCLE
#canvas.create_oval(2,251, 251,2, fill='green')

#CREATING ARC
#canvas.create_arc(0,0, 500,500, fill='purple', style=tk.PIESLICE, start=270, extent=180)

#CREATING POKEY BALL
canvas.create_arc(0,0, 500,500, fill='red', extent=180, width=10)
canvas.create_arc(0,0, 500,500, fill='white', extent=180, start= 180, width=10)
canvas.create_oval(190,190, 310,310, fill='white', width=10)

window.mainloop()