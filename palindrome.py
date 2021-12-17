num = int(input("Enter the number to be reverse : "));
reverse = 0;
num1 = 0;
num1 = num;
while num > 0 :
    reverse = int((reverse * 10) + (num % 10));
    num //= 10;
print("The reversed number is : ", reverse);
if reverse == num1:
    print("This is a palindrome number");
else:
    print("This is NOT a palindrome number");





#     num = int(input("Enter the number to be reverse : "));
# ans = 0;
# num1 = 0;
# num = num1;
# while num > 0 :
#     rem = num % 10;
#     ans = ans + (rem ** 3);
#     num //= 10;
# print("The cubic number is : ", int(ans));
# if num1 == num:
#     print("This is a armstrong number");
# else:
#     print("This is NOT a armstrong number");