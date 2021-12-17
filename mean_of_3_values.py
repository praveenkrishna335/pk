a = int(input("Enter the 1st number to get a mean : "));
b = int(input("Enter the 2nd number to get a mean : "));
c = int(input("Enter the 3rd number to get a mean : "));

if a > b :
    
    if a < c :
        median = a;
    elif b > c:
        median = b;
    else :
        median = c;
else :
    if a > c :
        median = a;
    elif b < c :
        median = b;
    else :
        median = c;
print("The median of the THREE values is : ", median);