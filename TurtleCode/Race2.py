#Turtle race game 
#Importing Require Library
from ast import Num
import turtle 
import random
import time

#Create Screen
def CreateGround(name,color):
    screen=turtle.Screen()
    screen.bgcolor(color)
    return screen
#ground=CreateGround("ground","red")
#Create Player
def CreatePlayer(player,shap,pcolor):
    #player=turtle.Turtle()
    player.shape(shap)
    player.color(pcolor)
    player.penup()
    return player
num=int(input("Enter How many Player use want to create"))
player = [turtle.Turtle() for _ in range(num)]
for i in range(num):
    color=input("Enter Player Color")
    shap=input("Enter Player Shape")
    player[i]=CreatePlayer(player[i],shap,color)






#turtle.done()