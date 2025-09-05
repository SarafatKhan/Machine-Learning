import random

def game():
    highScore = random.randint(1,100)
    return highScore

with open("highscore.txt", "r") as f:
    oldHighScore = int(f.read())

print("Your are Playing the game!!")
newScore = game()
print(f"Your new score is {newScore}")
print(f"Old High score is {oldHighScore}")
with open("highscore.txt", "w") as f:
    if(newScore > oldHighScore):
        oldHighScore = newScore
    print(f"Final High score is {oldHighScore}")
    if(oldHighScore == 100):
        f.write(str(0))
    else:
        f.write(str(oldHighScore))

