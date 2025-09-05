import pyttsx3

engine = pyttsx3.init()
"""
name = input("Whtat is your name: ")
print("Good afternoon " + name)

print(f"Good afternoon {name}")
"""
# 2.
# Dear Name 
# you are selected
# date

"""
date = input("Enter a date: ")
string = '''Dear Name
You are selected
Date'''
print(string)

changedString = string.replace("Name", name).replace("Date", date)
print(changedString)
engine.say(changedString)
engine.runAndWait()

"""
# 3. detect double space or find index of specific word

str1 = "This is a random line for learnig  something new."

index1 = str1.find("  ")
index2 = str1.find("new")
print(index1)
print(index2)

str2=str1.replace("  ", " ")
print(str1)
print(str2)