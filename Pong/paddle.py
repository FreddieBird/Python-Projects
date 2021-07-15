from turtle import Turtle


PADDLE_MOVE = 20

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def move_up(self):
        """Moves paddle upwards."""
        position = (self.xcor(), min(self.ycor()+PADDLE_MOVE, 250))
        self.goto(position)


    def move_down(self):
        """Moves paddle downwards."""
        position = (self.xcor(), max(self.ycor()-PADDLE_MOVE, -250))
        self.goto(position)
