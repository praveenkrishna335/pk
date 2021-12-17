num = int(input("Enter the number to be perform : "))
q = num
s=['0'] *100
i = 0
while q != 0 :
    rem = q % 16
    if rem < 10 :
        s[i] = chr(48 + rem)
        i += 1
    else :
        s[i] = chr(55 + rem)
        i += 1
    q //= 16
# for i in range()
j = i - 1
print("The hexadecimal number is : ",end='')
while j >= 0 :
    
    print( s[j],end='')
    j = j - 1