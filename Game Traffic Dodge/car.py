## Car builder

from turtle import Turtle
import random


colors = ["red", "blue", "green", "yellow", "purple", "magenta", "violet", "springgreen", "coral"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        rand_color = random.choice(colors)
        self.color(rand_color)
        rand_y = random.randint(-260, 260)
        self.goto(300, rand_y)


    def move_left(self):
        """Moves the car left a random amount."""
        rand_dis = random.randint(0, 10)
        self.goto(self.xcor()-rand_dis, self.ycor())
