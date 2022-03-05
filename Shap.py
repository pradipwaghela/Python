from turtle import *
import turtle        
wn=turtle.Screen()
wn.bgcolor("green")
wn.title("Shape")
shape=turtle.Turtle()
shape.fillcolor("black")
shape.speed(1)

for i in range(4):
    turtle.up
    shape.left(90)
    shape.forward(100)
    turtle.down

turtle.done()
