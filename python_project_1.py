import random
'''1 for snake
-1 for water
0 for gun'''
computer = random.choice([-1, 0, 1])

youstr = input("enter your choice snake(-1),water(1),gun(0):").lower()

youdict = {"snake": 1, "water": -1, "gun": 0}

reversedict = {1: "snake", -1: "water", 0:"gun"}
#Validate user input to prevent crashes
if youstr not in youdict:
    print("invalid choice! please type snake, water , or gun.")
else:    
 you = youdict[youstr]

print(f"\nyou chose: {reversedict[you]}")
print(f"computer chose: {reversedict[computer]}\n")

#Game Logic

if(computer==you):
    print("it is a draw!!")
else:
    #simplified math formula for snake-water-gun resolution
    if(computer==-1 and you==1):  #Snake Drinks Water
        print("you win!")

    elif(computer==-1 and you==0): #Water Drowns Gun
        print("you lose!")

    elif(computer==1 and you==0):  #Gun Kills Snake
        print("you win!")

    elif(computer==1 and you==-1): #Snake Drinks Water
        print("you lose!")

    elif(computer==0 and you==-1): #Water Drowns Gun
        print("you win!")

    elif(computer==0 and you==1): #Gun Kills Snake
        print("you lose!")

    else:
        print("something went wrong!!")
        


import random
'''1 for snake
-1 for water
0 for gun'''
computer = random.choice([-1, 0, 1])

youstr = input("enter your choice snake(-1),water(1),gun(0):").lower()

youdict = {"snake": 1, "water": -1, "gun": 0}

reversedict = {1: "snake", -1: "water", 0:"gun"}
#Validate user input to prevent crashes
if youstr not in youdict:
    print("invalid choice! please type snake, water , or gun.")
else:    
 you = youdict[youstr]

print(f"\nyou chose: {reversedict[you]}")
print(f"computer chose: {reversedict[computer]}\n")

#Game Logic

if(computer==you):
    print("it is a draw!!")
else:
    #simplified math formula for snake-water-gun resolution
    if(computer==-1 and you==1):  #Snake Drinks Water
        print("you win!")

    elif(computer==-1 and you==0): #Water Drowns Gun
        print("you lose!")

    elif(computer==1 and you==0):  #Gun Kills Snake
        print("you win!")

    elif(computer==1 and you==-1): #Snake Drinks Water
        print("you lose!")

    elif(computer==0 and you==-1): #Water Drowns Gun
        print("you win!")

    elif(computer==0 and you==1): #Gun Kills Snake
        print("you lose!")

    else:
        print("something went wrong!!")
        


