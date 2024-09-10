class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = self.canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        ball_coordinates = self.canvas.coords(self.image)

        if ball_coordinates[2] >= self.canvas.winfo_width() or ball_coordinates[0] < 0:
            self.xVelocity = -self.xVelocity

        if ball_coordinates[3] >= self.canvas.winfo_height() or ball_coordinates[1] < 0:
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)