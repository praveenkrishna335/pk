num = int(input("Enter the number to be perform : "));

a = int(num % 3);
b = int(num % 7);
print(a,b);
if (a and b) == 0 :
    print("The number is divided by 3 and 7");
else:
    print("The number is not divided by 3 and 7");