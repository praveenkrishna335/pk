num = int(input("Enter the number to be reverse : "));
reverse = 0;
while num > 0 :
    reverse = (reverse * 10) + (num % 10);
    num //= 10;
print("The reversed number is : ", int(reverse));