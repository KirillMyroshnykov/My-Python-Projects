from tkinter import *
import random
import pygame

#GAME CONSTANTS
GAME_WIDTH = 1000
GAME_HEIGHT = 800
SPEED = 80         # The lower the number, the faster the game
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'
MUSIC_1 = 'gameover.mp3'
MUSIC_2 = 'eating_apple.mp3'

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
            self.squares.append(square)

class Food:
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if initial_direction == 'up':
        y -= SPACE_SIZE

    elif initial_direction == 'down':
        y += SPACE_SIZE

    elif initial_direction == 'left':
        x -= SPACE_SIZE

    elif initial_direction == 'right':
        x += SPACE_SIZE

    # After eating a food the snake's body will be increased
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1

        label.config(text=f'Score:{score}')

        canvas.delete('food')
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_2)    #Addind eating sound
        pygame.mixer.music.play()
        food = Food()

    #Otherwise the last part of snake's body will be deleted while the snake is moving
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global initial_direction

    if new_direction == 'up':
        if initial_direction != 'down':
            initial_direction = new_direction

    elif new_direction == 'down':
        if initial_direction != 'up':
            initial_direction = new_direction

    elif new_direction == 'left':
        if initial_direction != 'right':
            initial_direction = new_direction

    elif new_direction == 'right':
        if initial_direction != 'left':
            initial_direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2,
                       font=('consolas', 70), text='GAME OVER!!!', fill='red', tags='gameover')

    #ADDING A GAME OVER MUSIC
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_1)
    pygame.mixer.music.play()

window = Tk()
window.title('Snake game')
window.resizable(False, False)

score = 0
initial_direction = 'down'

label = Label(window, text=f'Score:{score}', font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

#WINDOW CENTERING
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

#BINDING KEYS
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()