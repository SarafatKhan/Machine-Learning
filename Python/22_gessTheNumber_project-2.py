import random

rn = random.randint(1, 100)
num = int(input("Guiss the number: "))
score = 100
while(num != rn or num == "x"):
    print("Wrong!")
    score = score - 10
    if(num<rn):
        num = int(input("Your no. is small, choose large: "))
    else:
        num = int(input("Your no. is large, Try small: "))
if(num == rn):
    print("Congratulations! You Won")
    print(f"Your score is : {score} !!")
else:
    print("You play good!, but not win!")



















  






























































































































