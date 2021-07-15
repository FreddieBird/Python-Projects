## Drawing shapes using Turtle

from turtle import Turtle, Screen
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(turtle, sides):
    """Draws any shape given the number of sides."""
    angle = 360 / sides

    for i in range(sides):
        turtle.forward(100)
        turtle.left(angle)



def main():
    turtle = Turtle()
    screen = Screen()
    turtle.shape("turtle")

    for i in range(3,10):
        turtle.color(random.choice(colors))
        draw_shape(turtle, i)


    screen.exitonclick()


if __name__=='__main__':
    main()
