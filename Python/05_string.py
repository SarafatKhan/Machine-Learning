oldString1 = 'Sallu bhai'
oldString2 = "Sallu bhai"
oldString3 = '''Sallu bhai'''

print(oldString1 + " " + oldString2 + " " + oldString3)

firstName = oldString1[0:5]
secondName = oldString1[6:10]

firstName2 = oldString1[:5]
secondName2 = oldString1[6:]

print(firstName)
print(secondName)

print(firstName2)
print(secondName2)


# skip value 

numString = "123456789"
charString = "This is a random string"

skipString = numString[2:8:2]
skipCharString = charString[2:15:3]

print(skipString)
print(skipCharString)


# ----------------------------------String---Function----------