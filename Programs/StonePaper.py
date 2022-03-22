"""
0=Rock
1=Paper
2=Scissor
"""

import random

Comp=random.randint(0,2)
Winner=''
User=int(input(print("Rock Paper Scissors (0,1,2)")))
if (User == Comp):
    Winner="Tie"
elif(Comp == 0) and (User ==2):
    Winner="Computer"
elif (Comp==1) and (User== 0):
    Winner="Computer"
elif(Comp==2) and (User==1):
    Winner="Computer"
else:
    Winner="User"

if(Winner=="Tie"):
    print(Winner,"Both are same")
else:
    print(Winner,"Won,Computer Chose",Choice(Comp))



def Choice(num):
    if num==0:
        return "Rock"
    elif num==1:
        return "Paper"
    elif num==2:
        return "Scissor"