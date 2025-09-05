foods = ["Apple", "Nanana", "Rice", "Brade", 305, 'D', 44.43]
print(foods)
print(foods[1:4])

foods[4] = "books"
print(foods)


# -----------------------------List----Functions-------


# 1. Append

foods.append("bigg boss")
print(foods)

# 2. insert

foods.insert(5,"Moon")
print(foods)

# 3. extend

material = ["iron", "silver", 34, "Hydrozen"]
print(material)
foods.extend(material)

print(foods)

# 4. pop

print(foods.pop())
print(foods)

# 5.reverse

foods.reverse()
print(foods)

# 6. index

print(foods.index("books"))

# 7.count

print(foods.count("D"))

# 8. sort -- its only works when all charactors are string or int or any other

# 9. remove

print(foods.remove("Rice"))
print(foods)

# 10. copy

lunch = foods.copy()
print(lunch)

# 11. length

print(len(foods))

# 12.  all and any

print(all(foods))
print(any(foods))

# 13. enumerate 

for i, food in enumerate(foods):
    print(i, food)

# 14. zip 

lunch.reverse()

newPairList = list(zip(foods,lunch))

for j, newP in enumerate(newPairList):
    print(j,newP)

# 15. slice 

dinner = foods[0:5]
print(dinner)


# ---------Map---and---Filter----------

numList = [2,4,5]

makeSquare = list(map(lambda x: x**2, numList))
print(makeSquare)

numList.append(6)
numList.append(8)
numList.append(9)
numList.append(11)
print(numList)

findEven = list(filter(lambda x: x % 2 == 0, numList))
print(findEven)

fruits = ["apple", "banana", "mango", 1, "hello", True, 3.14]
