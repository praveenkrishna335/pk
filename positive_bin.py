start = int(input("Enter the start value : "))
stop = int(input("Enter the stop value : "))
binary = 0
for i in range(start,stop) :
    if i <= 0 :
        print("Please print different (or) a positive number")
    else :
        # rem = i % 2
        binary = (binary * 10) + i
print("the binary number ",i," is : ", binary)
    