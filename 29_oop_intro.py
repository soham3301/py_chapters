import turtle
import tkinter as TK
import prettytable
import random

raphael = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.bgcolor("black")

raphael.shape("turtle")
raphael.color("SpringGreen")
raphael.pensize(15)


table = prettytable.PrettyTable()




directions = [0, 90 ,180, 270]

for _ in range(200):
    raphael.forward(30)
    raphael.setheading(random.choice(directions))






































raphael.forward(100)
my_screen.exitonclick()
