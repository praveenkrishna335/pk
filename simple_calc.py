num = int(input("Enter a number : "))

while num > 0 :
    ans2 = num ** 2
    ans3 = num ** 3
    ans4 = num ** 4
    num //= 10
print("The answer for x^2 is : ", ans2)
print("The answer for x^3 is : ", ans3)
print("The answer for x^4 is : ", ans4)