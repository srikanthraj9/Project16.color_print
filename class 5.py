# how  to generate random rgb colour
import turtle
import random
from turtle import Turtle,Screen

timmy = Turtle()
timmy.pensize(15)
turtle.colormode(255)

direction = [30,60,90,120,180]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(100):
    timmy.color(random_color())
    timmy.forward(10)
    timmy.setheading(random.choice(direction))
screen = Screen()
screen.exitonclick()