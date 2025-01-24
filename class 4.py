import random
from turtle import Turtle,Screen

timmy = Turtle()
timmy.pensize(15)
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "cyan",
    "magenta"
]
directions = [30,60,90,120,180]
for _ in range(1000):
    timmy.forward(50)
    timmy.right(random.choice(directions))
    timmy.color(random.choice(colors))
    timmy.forward(50)


screen = Screen()
screen.exitonclick()