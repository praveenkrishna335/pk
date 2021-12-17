num = int(input("Enter the number to be perform : "));
ans = 0;
num1 = 0;
num1 = num;
while num > 0 :
    rem = num % 2;
    ans = ans*10+int(rem);
    num //= 2;
print("The binary number of ", num1 ," is : ", ans);
