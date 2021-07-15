## Draws a spirograph using Turtle module

from turtle import Turtle, Screen
import random

def main():

    turtle = Turtle()
    screen = Screen()

    turtle.speed(20)
    angle = 0
    while angle != 360:
        turtle.pencolor((random.random(), random.random(), random.random()))
        turtle.setheading(angle)
        turtle.circle(80)
        angle += 5


    screen.exitonclick()

if __name__=='__main__':
    main()
