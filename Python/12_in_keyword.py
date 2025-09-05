s1 = "click this link"
s2 = "free register"
s3 = "make million in one day"
s4 = "click now"
s5 = "free free"

mail = input("Enter the statement that you want to mail: ")
if((s1 in mail) or (s2 in mail) or (s3 in mail) or (s4 in mail) or (s5 in mail)):
    print("This is a spam mail")
else:
    print("Thanks for mail")

listName = ["rohan", "sohan", "diljeet", "dipak"]
name = input("Etner your name: ")

if(name in listName):
    print("Your name is in the list.")
else:
    print("your name is not in the list.")