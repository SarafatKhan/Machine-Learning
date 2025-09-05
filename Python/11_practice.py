hindiToEnglish = {
    "kitabe": "books",
    "pankha" : "fan",
    "raat": "night"
}

print(hindiToEnglish.get("kitabe"))

language = {
    "rohan" : "english",
    "sohan": "hindi",
    "veer": "gujarati",
    "diljeet": "urdu"
}

print(language.get("veer"))

codingSkill = {}

while(codingSkill.get("exit") != "exit"):
    name = input("Write name: ")
    skill = input("Write skill: ")
    codingSkill.update({name:skill})
print(codingSkill)


# print(hash(42))               # 42
# print(hash("hello"))          # hash of string
# print(hash((1, 2, 3)))        # tuple of hashables
# print(hash(frozenset([1, 2])))# OK

for i in codingSkill:
    print(f"{i} skilled in {codingSkill.get(i)}")