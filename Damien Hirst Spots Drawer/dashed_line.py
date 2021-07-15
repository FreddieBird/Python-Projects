## Draws a dashed line using Turtle

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.color("coral")
turtle.shape("turtle")

for i in range(6):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

screen.exitonclick()
