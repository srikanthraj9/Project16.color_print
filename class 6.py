import random
import turtle
from turtle import Turtle,Screen
import random

timmy = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color  = (r,g,b)
    return color

timmy.speed("fastest")
def size_of_directions(gap):
    for  _ in range (int(360/gap)):
        timmy.color(random_color())
        timmy.circle(200)
        timmy.setheading(timmy.heading() + gap)

size_of_directions(5)

screen = Screen()
screen.exitonclick()