from turtle import  Turtle,Screen

timmy = Turtle()#.shape("turtle")
timmy.shape("turtle")
timmy.color("red")
def angle():
    timmy.left(120)
def triangle():
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
for _ in range(3):
    triangle()
    angle()

screen = Screen()
screen.exitonclick()