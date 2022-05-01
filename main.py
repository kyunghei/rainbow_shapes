from turtle import Turtle, Screen

tim = Turtle()


def triangle():
    tim.color("red")
    for _ in range(3):
        tim.forward(100)
        tim.left(120)


def square():
    tim.color("orange")
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


def pentagon():
    tim.color("yellow")
    for _ in range(5):
        tim.forward(100)
        tim.left(72)


def hexagon():
    tim.color("green")
    for _ in range(6):
        tim.forward(100)
        tim.left(60)


def heptagon():
    tim.color("blue")
    for _ in range(7):
        tim.forward(100)
        tim.left(51.43)


def octagon():
    tim.color("navy")
    for _ in range(8):
        tim.forward(100)
        tim.left(45)


def nonagon():
    tim.color("purple")
    for _ in range(9):
        tim.forward(100)
        tim.left(40)


def decagon():
    tim.color("black")
    for _ in range(10):
        tim.forward(100)
        tim.left(36)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
decagon()

screen = Screen()
screen.exitonclick()
