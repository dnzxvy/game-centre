from tkinter import *
from tkinter import messagebox
import random
import pygame


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])  # by doing [0, 0] at the start of every game, the snake will
            # appear on the top left hand corner

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):
        x = random.randint(0,
                           int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE  # ihad to put int because it can produce a float value if
        # game_width is not a multiple of space_size which did happen so by converting it to
        # an integer it works.
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")
        # x,y is the starting corner and the ending corner which would be x and y plus the
        # space_size. this piece of code is for the food


def start_game():
    pygame.mixer.music.load("protected.mp3")  # Replace with the path to your music file
    pygame.mixer.music.play(-1)  # -1 plays the music in an infinite loop

    global snake, food
    snake = Snake()
    food = Food()
    next_turn(snake, food)

    start_button.destroy()

    game_over_label.place_forget()
    restart_button.place_forget()


def restart_game():
    global score
    score = 0
    label.config(text="Score:{}".format(score))
    game_over_label.place_forget()
    restart_button.place_forget()
    start_game()


GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 65
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":  # these are the directions that the snake can take
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)

    snake.squares.insert(0, square)  # updating the snakes list of squares

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        # the code above with del is to delete the last body part of the snake so it can move
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction  # the global keyword is used so that a variable belongs to the
    # global scope instead of just normal variable that are local and can only be
    # used inside that function
    if new_direction == 'left':
        if direction != 'right':  # != means does not
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


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
    # canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,

    # font=('consolas',70), text="GAME OVER", fill="purple", tag="gameover")

    game_over_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    restart_button.place(relx=0.5, rely=0.6, anchor=CENTER)


window = Tk()
window.title("Snake game")  # .title method is where the first character in every
# word is uppercase
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))  # .format method formats the
# specified values and insert them inside the string's placeholder (this is the placeholder{})
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack(fill=BOTH, expand=True)

start_button = Button(window, text="Start Game", font=('consolas', 20), command=start_game, bd=0)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
window.update()  # this is to update the window so it renders

game_over_label = Label(window, text="Game Over!", font=('consolas', 40), fg="red")
restart_button = Button(window, text="Restart Game", font=('consolas', 20), command=restart_game, bd=0)
restart_button.place_forget()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()  # returns screen height in pixels
screen_height = window.winfo_screenheight()  # returns the screen width in pixels

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# thecode above this is to help update the snake game window so when it opens it
# appears on the middle of the screen

window.bind('<Left>', lambda event: change_direction('left'))  # .bind is used so you can bind things to keys
# on the keyboard. lambda is used inside any function that works as an anonymous function
# lambda can also be used to pass data to a callback function
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

pygame.init()
pygame.mixer.init()

window.mainloop()
