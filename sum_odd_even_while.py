num = int(input("Enter the number to be perform : "))
odd = num
num1 = 0
while num > 0 :
    rem = num % 10
    if  (rem % 2) == 0 :
        num1 = num1 + rem
    num //= 10
print("The Sum Of EVEN Values Are : ",num1)

num2 = 0
while odd > 0 :
    rem1 = odd % 10
    if  (rem1 % 2) != 0 :
        num2 = num2 + rem1
    odd //= 10
print("The Sum Of ODD Values Are : ",num2)