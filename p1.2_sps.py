import random
#Random Number 
Ran_num=random.randint(0,2)

#Determining computers choice
if (Ran_num==0):
    Comp_ch="stone"
elif (Ran_num==1):
    Comp_ch="paper"
else:
    Comp_ch="scissors"

#User choice
Use_ch = ''
while (Use_ch != 'stone' and
Use_ch != 'paper' and
Use_ch != 'scissors'):
    Use_ch = input('Stone, Paper or Scissors? ').lower()

#Checking Winner
if (Comp_ch==Use_ch):
      winner="Tie"
elif(Comp_ch=="stone" and Use_ch=="scissors"):
    winner="Computer"
elif(Comp_ch=="paper" and Use_ch=="stone"):
    winner="Computer"
elif(Comp_ch=="scissors" and Use_ch=="paper"):
    winner="Computer"
else:
    winner="User"

#Printing Winner statement 
if winner=="Tie":
    print("Tie!!! Both chose",Comp_ch.title())
else:
    print(winner,"Won!!! The Computer chose \"",Comp_ch.title(),"\".")
