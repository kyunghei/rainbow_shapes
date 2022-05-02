from turtle import Turtle, Screen
import random
tim = Turtle()
colors = ["red", "orange", "yellow", "blue", "indigo", "violet", "green"]


def draw_shape(num_sides):
    degree = 360 / num_sides
    tim.color(random.choice(colors))
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(degree)


for elements in range(3,11):
    draw_shape(elements)

screen = Screen()
screen.exitonclick()
