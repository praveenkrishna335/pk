num = int(input("Enter the number to be perform : "))

ans = 0
i = 0

while num > 0 :
    rem = num % 10
    temp = rem * (2 ** (i))
    i += 1
    num //= 10
    ans += temp
print("The octal number is : ", ans)