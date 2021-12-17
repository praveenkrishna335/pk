ip = int(input("Enter the length : "))
list1 = []

for i in range(ip) :
    num = int(input("Enter the number : "))
    list1.append(num)
print(list1)

for i in list1 :
    if i >= 0 :
        if (i % 2) == 0 :
            print("The even number is : ", i)

        if (i % 2) != 0 :
            print("The odd number is : ", i)
maximum = max(0,i)
print("The maximum value is : ", maximum)

for i in list1 :
    if i < 0 :
        print("The number {i} is a Negative number")
