# 100 days of code - Day 4
import random

rock = ''' '''
paper= ''' '''
scissors = ''' '''



print("0 = rock\n 1 = Paper\n 2= Scissors\n")
player=input("Choose between rock, paper or scissors to play.  \n ")
playerformat=player.lower()
print (playerformat)

computer=random.randint(0,2)

if player==0:
    print(rock)
elif player==1:
    print(paper)
elif player==2:
    print(scissors)
else:
    print("invalid")


print("Computer chose: ", computer)
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
elif computer==2:
    print(scissors)


if computer==player:
    print("It's a tie!")
elif computer==0 and player==1:
    print("You Win!")
elif computer==1 and player==2:
    print("You Win!")
elif computer==2 and player == 0:
    print("You Win!")
else:
    print("You Loose")




print(computer)
print(rock)
print(scissors)


