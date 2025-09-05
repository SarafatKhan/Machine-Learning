for i in range(1,5):
    print(i)
    if(i==4):
        break

num = int(input("Enter a number: "))
for i in range(2,num):
    if(num%i == 0):
        print(i)
        print("number is not prime")
        break
else:
    print("number is prime")