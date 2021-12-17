num = int(input("Enter the list length : "))
list1 = []
list2 = []
for i in range(num):
    num1 = int(input("Enter the number : "))
    list1.append(num1)
    list2.append(num1)

num1 = 0
for even in list1 :
    if  (even % 2) == 0 :
        num1 = num1 + even
print("even",num1)

num2 = 0
for odd in list2 :
    if (odd % 2) != 0 :
        num2 = num2 + odd
print("odd",num2)