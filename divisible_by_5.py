start = int(input("Enter the start number : "))
stop = int(input("Enter the stop number : "))
temp = 0
for i in range(start,stop + 1) :
    if (i % 5) == 0 :
        print("The number which is divisible by 5 is : ", i)
        temp = temp + i
print("The total of divisible number is : ", temp)

