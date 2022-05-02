from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r, b, g)


tim = Turtle()
tim.pensize(10)
tim.speed(50)
degrees = [0, 90, 180, 270]
for _ in range(300):
    tim.pencolor(random_color())
    tim.forward(25)
    tim.left(random.choice(degrees))





screen = Screen()
screen.exitonclick()