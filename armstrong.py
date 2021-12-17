num = int(input("Enter the number to be perform : "))
ans = 0
num1 = 0
num1 = num
while num > 0 :
    rem = num % 10
    ans = int(ans + (rem ** 3))
    num //= 10
print("The output number is : ", ans)
if ans == num1:
    print("This is a armstrong number")
else:
    print("This is NOT a armstrong number")