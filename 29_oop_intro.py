import turtle
import tkinter as TK
import prettytable

raphael = turtle.Turtle()
my_screen = turtle.Screen()

raphael.shape("turtle")
raphael.color("red")

raphael.forward(100)
my_screen.exitonclick()

table = prettytable.PrettyTable()