## Random walk using Turtle module

from turtle import Turtle, Screen
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


def random_grid_walk(turtle):
    """Randomly moves the turtle around a grid."""
    #turtle.color(random.choice(colors)) # set color
    turtle.pencolor((random.random(), random.random(), random.random()))
    turtle.forward(30) # move forward
    turtle.setheading(random.choice(directions)) # random turn

def random_walk(turtle):
    """Randomly moves the turtle around the screen."""
    #turtle.color(random.choice(colors)) # set color
    turtle.pencolor((random.random(), random.random(), random.random()))

    # move forward a random distance
    turtle.forward(random.randint(0, 10))

    # randomly turn left or right
    turn = random.randint(0,1)
    angle = random.randint(0, 90)
    if turn == 0:
        # turn left
        turtle.left(angle)
    elif turn == 1:
        # turn right
        turtle.right(angle)


def main():
    turtle = Turtle()
    screen = Screen()

    turtle.pensize(10)
    turtle.speed(9)

    for i in range(200):
        #random_walk(turtle)
        random_grid_walk(turtle)


if __name__=='__main__':
    main()
