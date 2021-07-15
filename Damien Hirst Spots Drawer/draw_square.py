## Draws a square using Turtle module

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


for i in range(4):
    turtle.forward(200)
    turtle.left(90)
    
screen.exitonclick()
