# limit = int(input("Enter the limit : "))

# fib = int(input("Enter the x value : "))
# prime = int(input("Enter the n value : "))

# For prime numbers...
a = int(input("Enter an input number:"))
num = a
if a > 1:  
    for j in range(2, int(a/2) + 1):  
        if (a % j) != 0:
            pass
    print("prime is : ", j)
# For fibonacci series
n1 = 0
n2 = 1

for i in range(2,num) :
    x = n1 + n2
    n1 = n2
    n2 = x
print("fibonacci is : ", n2)
