from turtle import Turtle,Screen
import random
timmy = Turtle()
timmy.shape("turtle")
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

def creating_shapes(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3,12):
    creating_shapes(sides)
    timmy.color(random.choice(colors))



screen = Screen()
screen.exitonclick()
screen.screensize(1000,1000)