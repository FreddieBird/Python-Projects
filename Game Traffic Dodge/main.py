## Turtle crossing game
from turtle import Turtle, Screen
from player import Player
from car import Car
from levelboard import Levelboard
from time import sleep
import random

START_DIFFICULTY = 15

screen = Screen()


def reset():
    screen.clear()
    main()


def main():
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("El Classico Turtle Crossing Game")
    screen.tracer(0)

    # create player
    player = Player()

    # create levelboard
    levelboard = Levelboard()

    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.onkey(reset, "r")

    game_is_on = True
    cars = []
    while game_is_on:
        sleep(0.01)
        screen.update()

        # chance to create random car
        rand_chance = random.randint(1,START_DIFFICULTY-levelboard.level)
        if rand_chance < 1:
            rand_chance == 1
        if rand_chance == 1:
            car = Car()
            cars.append(car)


        # move player back to start when finish line is reached
        if player.ycor() >= 280:
            levelboard.update_levelboard()
            player.reset()
            continue


        # loop over cars and randomly move them along x-axis
        # also check for collisions
        for c in cars:
            # move car left
            c.move_left()

            # checl for collisions
            if player.distance(c) < 20:
                levelboard.game_over()
                game_is_on = False


    screen.exitonclick()


if __name__ == '__main__':
    main()
