## Player class

from turtle import Turtle

MOVE_DIS = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)


    def move_up(self):
        """Moves player up."""
        self.goto(0, self.ycor()+MOVE_DIS)


    def move_down(self):
        """Moves player down."""
        if self.ycor() >= -280 + MOVE_DIS:
            self.goto(0, self.ycor()-MOVE_DIS)


    def reset(self):
        """Moves player back to start."""
        self.goto(0, -280)
