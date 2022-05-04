# 100 days of code - Day 3
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("You're at a cross road. Where do you want to go? Type ""left"" or ""right""").lower()
if (choice1 =="left"):
    choice2= input("You have come to a lake, swim or wait? ")
    if (choice2 == "wait"):
        choice3= input("There are three doors, Red, Blue and Yellow. Which one will you choose? ").lower()
        if(choice3=="Yellow"):
            print("You Win!")
        elif(choice3== "Red"):
            print("Game Over.")
        elif(choice3=="Blue"):
            print("Game Over.")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")




