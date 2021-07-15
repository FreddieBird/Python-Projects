## Keeps track of current level

from turtle import Turtle

class Levelboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_levelboard()


    def update_levelboard(self):
        self.level += 1
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 18, "bold"))


    def game_over(self):
        """Ends game."""
        self.goto(0, 0)
        self.write(f"GAME OVER...press 'r' to player again.", align="center", font=("Courier", 16, "bold"))
