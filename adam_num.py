num = int(input("Enter the number to check : "));
sq = 0;
sq = sq + (num ** 2);
reverse = 0;
while sq > 0 :
    reverse = int((reverse * 10) + (sq % 10));
    sq //= 10;
print("The reversed square number is : ", reverse);

sqrt = int(reverse ** (1/2));
print("The sqrt number is : ", sqrt);

reverse1 = 0;
while sqrt > 0 :
    reverse1 = int((reverse1 * 10) + (sqrt % 10));
    sqrt //= 10;
print("The reversed sqrt number is : ", reverse1);

if reverse1 == num :
    print("This is a Adam number");
else :
    print("This is NOT a Adam number");