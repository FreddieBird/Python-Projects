from time import sleep
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random

screen = Screen()

def main():
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("El Classico Pong Game")
    screen.tracer(0)

    # Create paddles
    paddle_1 = Paddle(-350, 0)
    paddle_2 = Paddle(350, 0)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(paddle_1.move_up, "w")
    screen.onkey(paddle_1.move_down, "s")
    screen.onkey(paddle_2.move_up, "Up")
    screen.onkey(paddle_2.move_down, "Down")

    game_is_on = True
    while game_is_on:
        sleep(ball.move_speed)
        screen.update()
        ball.move()

        # detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce('wall')


        # detect collision with left paddle
        if (ball.xcor() - paddle_1.xcor() > 0) and (ball.xcor() - paddle_1.xcor() < 25) and (abs(ball.ycor() - paddle_1.ycor()) < 80):
            ball.bounce('paddle')

        # detect collision with right paddle
        if (paddle_2.xcor() - ball.xcor() > 0) and (paddle_2.xcor() - ball.xcor() < 25) and (abs(ball.ycor() - paddle_2.ycor()) < 80):
            ball.bounce('paddle')

        # detect if ball goes out-of-bounds
        if ball.xcor() > paddle_2.xcor() + 50:
            scoreboard.increase_l_score()
            ball.reset()
        elif ball.xcor() < paddle_1.xcor() - 50:
            scoreboard.increase_r_score()
            ball.reset()


    screen.exitonclick()

if __name__=='__main__':
    main()
