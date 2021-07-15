from turtle import Turtle

BALL_MOVE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_MOVE
        self.y_move = BALL_MOVE
        self.move_speed = 0.1

    def move(self):
        """Moves the ball."""
        position = (self.xcor()+self.x_move, self.ycor()+self.y_move)
        self.goto(position)


    def bounce(self, object):
        """Bounces ball from top/bottom."""
        if object == 'wall':
            self.y_move *= -1
        elif object == 'paddle':
            self.x_move *= -1
            self.move_speed *= 0.9


    def reset(self):
        """Resets the ball to the middle of screen
        and change direction of ball."""
        self.x_move *= -1
        self.goto(0, 0)
        self.move_speed = 0.1
