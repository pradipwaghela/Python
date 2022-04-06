#Turtle race game 
#Importing Require Library
import turtle 
import random
import time
#Set up screen 
screen=turtle.Screen()
screen.bgcolor("lightblue")
#Set up Player
def CreatePlayer(player,shap,pcolor):
    player=turtle.Turtle()
    player.shape(shap)
    player.color(pcolor)
    player.penup()
    return player

#Print Position
def PrintPosition(p1,p2,line):
    print("-------------")
    print("Player 1",p1.pos())
    print("Player 2 ",p2.pos())
    print("Line ",line.pos())
    print("-------------")

#Create Player
p1=CreatePlayer("p1","turtle","red")
p2=CreatePlayer("p2","turtle","blue")

#Set Position
p1.goto(-300,100)
p2.goto(-300,50)

#Finish Line Setup
line=CreatePlayer("line","circle","black")
line.goto(250,-200)
line.left(90)
line.pendown()
line.forward(400)
line.write("Finish",font=24)
line.hideturtle()

#Lets Play Game
p1.pendown()
p2.pendown()
dice=[1,2,3,4,5,6]
for i in range(30):
    if p1.pos() >= (250,100):
        print("Player One Won!!")
        break
    elif p2.pos() >= (250,50):
        print("Player Two won!!")
        break
    else:
        PrintPosition(p1,p2,line)
        move=random.choice(dice)
        p1.forward(10*move)
        time.sleep(1)
        move=random.choice(dice)
        p2.forward(10*move)
        time.sleep(1)
PrintPosition(p1,p2,line)

#Turtle Runing
turtle.done()