from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed(50)
colors = ["red", "pink", "light blue", "orange", "violet", "purple", "green", "aqua"]
degrees = [0, 90, 180, 270]
for _ in range(300):
    tim.color(random.choice(colors))
    tim.forward(25)
    tim.left(random.choice(degrees))





screen = Screen()
screen.exitonclick()