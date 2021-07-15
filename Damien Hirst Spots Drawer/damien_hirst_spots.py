## Draws a damien hirst inspired painting using Turtle

from turtle import Turtle, Screen, colormode
import random
import colorgram

colormode(255)

def get_colors(image, num_colors):
    """Gets a list of rgb values from a given image."""
    colors = colorgram.extract(image, num_colors)
    rgbs = []
    for c in range(num_colors):
        rgbs.append(colors[c].rgb)

    return rgbs


def draw_dots(turtle, screen, rgbs):
    """Draws a damien hirst inspired image."""

    # keep going until at top of canvas
    while turtle.pos()[1] < 300:
        # select random color
        rgb = random.choice(rgbs)

        # if at end of width
        if turtle.pos()[0] >= screen.window_width():
            turtle.left(90)
            turtle.penup()
            turtle.forward(30)
            turtle.pendown()
            turtle.left(90)

        # if at beginning of width
        if turtle.pos()[0] <= -screen.window_width():
            turtle.right(90)
            turtle.penup()
            turtle.forward(30)
            turtle.pendown()
            turtle.right(90)

        # draw dot
        turtle.dot(15, (rgb[0], rgb[1], rgb[2]))
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()




def main():
    image = 'spots.jpg'
    rgbs = get_colors(image, 30)

    turtle = Turtle()
    screen = Screen()
    turtle.speed(20)
    turtle.penup()
    turtle.setpos(-screen.window_width(), -300)
    draw_dots(turtle, screen, rgbs)

    screen.exitonclick()

if __name__=='__main__':
    main()
