def adam(num):
    ans = 0
    while num > 0 :
        rem = num % 10
        ans = int(ans + (rem ** 3))
        num //= 10
    return ans
arg = int(input("Enter the number to be perform : "))
output = adam(arg)
print(output)