def removeName(fruites,fruit):
    newFruitList = []
    fruits.remove(fruit)
    for i in fruites:
        newFruitList.append(i.replace(fruit,""))
    return newFruitList
        

fruits = ["apple", "banana", "mango", "hello", "le"]

name = input("Which name you wants to remove: ")
newFruitList = removeName(fruits,name)
print(fruits)
print(newFruitList)
