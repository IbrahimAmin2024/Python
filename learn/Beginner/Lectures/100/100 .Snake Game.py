# Program in Python to create a Snake Game

import tkinter
from tkinter import *
import random

# Initialising Dimensions of Game
WIDTH = 500
HEIGHT = 500
SPEED = 200
SPACE_SIZE = 50
BODY_SIZE = 3
SNAKE = "blue"
FOOD = "white"
BACKGROUND = "black"
GAMEOVER = "maroon"
# Function to control direction of snake
def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

# Class to design the snake
class Snake:
    # Initialising
    # Creating for loop range of snake body to create list of coordinates(x,y)
    # Creating for loop to build the body snake use coordinates that we appended from the list

    def __init__(self):
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_SIZE):
            self.coordinates.append([0, 0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,
                                             x + SPACE_SIZE,
                                             y + SPACE_SIZE,
                                             fill=SNAKE,
                                             tags="snake"
                                             )
            self.squares.append(square)

        # print(self.squares)

        # Class to design the food
# Initialising
# Create Random Int(integer) num x,y Location Number
# Create Coordinate to check late if snake eaten the food successfully
# Create the food body use x,y coordinates
class Food:
    def __init__(self):
        x = random.randint(0,
                           (WIDTH/SPACE_SIZE) -1) * SPACE_SIZE
        y = random.randint(0,
                           (HEIGHT/SPACE_SIZE) -1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD,
                           tags="food"
                           )

def move(snake,food):
    x, y = snake.coordinates[0]  #head of the snake

    if direction == "up":
        y-= SPACE_SIZE
    elif direction == "down":
        y+= SPACE_SIZE

    elif direction == "left":
        x-= SPACE_SIZE

    elif direction == "right":
        x+= SPACE_SIZE

    # insert the coordinates
    snake.coordinates.insert(0, (x,y)) #coordinates

    # drawing the coordinates
    square = canvas.create_rectangle(
        x,y, x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE,
    )

    # insert the Squares, to drawable
    snake.squares.insert(0, square)

    # check if snake eaten the food.
    # if(old position of the food, new food location)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score+=1
        label.config(text=f"Points : {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # check if u hit the border , result as game over
    # hit_the_wall(snake)

    #if hit the wall statment
    if hit_the_wall(snake): #return ture
        game_over()
    else:
        my_screen.after(SPEED, move,snake,food)

def hit_the_wall(snake): #>= ,if stament

    x,y = snake.coordinates[0] #head of the snake

    if x < 0 or x >= WIDTH: # hit the left side, hit the right side.
        return True # after this call will return game over text
    elif y < 0 or y >= HEIGHT: # hit the top side, hit the bottom side.
        return True # after this call will return game over text

    #for loop for the whole snake body except the head.
    for snake_body in snake.coordinates[1:]:
      if x == snake_body[0] and y == snake_body[1]:
        return True

    return False # this remaining the function inifinitly work

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('comic Sans', 25),
                       text="You Lost, press Q to exit",
                       fill=GAMEOVER,
                       tags="gameover")


def Exit(_):
    my_screen.destroy()

# Giving title to the gaming window
my_screen = Tk()
# ===========
my_screen.title("Snake Game")
#direction of start moving
direction = "right"

# Display of Points Scored in Game
score = 0

label = Label(my_screen, text=("Score : {}".format(score)),
              font=("Comic Sans",18,"bold"))
label.pack()

canvas = Canvas(my_screen,bg=BACKGROUND,
                height=HEIGHT,
                width=WIDTH,)
canvas.pack()

my_screen.update()

new_x = ( int( (my_screen.winfo_screenwidth() / 2) - (my_screen.winfo_width() / 2) ) )
new_y = ( int( (my_screen.winfo_screenheight() / 2) - (my_screen.winfo_height() / 2) ) )
my_screen.geometry(f"{HEIGHT}x{WIDTH}+{new_x}+{new_y}")

#bind a key to change the snake direction

my_screen.bind("<Key-w>",
               lambda event: change_direction("up"))
my_screen.bind("<Key-a>",
               lambda event: change_direction("left"))

my_screen.bind("<Key-s>",
               lambda event: change_direction("down"))

my_screen.bind("<Key-d>",
               lambda event: change_direction("right"))

my_screen.bind("<Key-q>",
               lambda event: Exit(event))

# calling classes (snake,food)
snake = Snake()
food = Food()

#order to move the snake, and change food location
move(snake,food)
# ===========
my_screen.mainloop()