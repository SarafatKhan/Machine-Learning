allItems = []

num = int(input("How many elements you want to insert: "))
while num>0:
    item = input("Enter the Item: ")
    allItems.append(item)
    num -= 1
print("List:")
print(allItems)