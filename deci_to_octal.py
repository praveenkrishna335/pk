num = int(input("Enter the number to be perform : "));
ans = 0
s = []

while num > 0 :
    rem = num % 8
    ans = ans * 10 + rem
    num //= 8;
# s.append(ans)
# s.reverse()
# print(s)
reverse = 0
while ans > 0 :
    
    reverse = (reverse * 10) + (ans % 10)
    ans //= 10
print("the octal number is : ",reverse)
