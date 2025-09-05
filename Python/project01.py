'''
1 for Snack
-1 for Water
0 for Gun
'''
import random

computer = random.choice([1,-1,0])

youstr = input("Enter your choice: ")
gameDatabase = {"s": 1, "w":-1, "g":0}

gameDatabaseReverse = {1: "Snack", -1: "Water", 0: "Gun"}
you = gameDatabase[youstr]
print(f"You choose {gameDatabaseReverse[you]} \nAnd Computer choose {gameDatabaseReverse[computer]}")
if(computer == you):
    print("Game Draw!!")
else:
    if (computer == 1 and you == -1):  # computer - you = 2
        print("Computer Win!!")
    elif (computer == 1 and you == 0): # 1
        print("You Win!!")
    elif (computer == 0 and you == 1): # -1
        print("Computer Win!!")
    elif (computer == 0 and you == -1): # 1
        print("You Win!!")
    elif (computer == -1 and you == 0): # -1
        print("Computer Win!!")
    elif (computer == -1 and you == 1): # -2
        print("You Win!!")
    else:
        print("Something went Wrong!!")

# if((computer - you == -2) or (computer - you == 1)):
#     print("You win!!")
# else:
#     print("Computer win!!")