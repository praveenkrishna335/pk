def PrimeChecker(a):  
  
    if a > 1:  
        for j in range(2, int(a/2) + 1):  
            if (a % j) != 0:   
                if a == 3 :
                    print("INK PEN")
                if a == 5 :
                    print("BALL PEN")
                if a == 7 :
                    print("STICK PEN")
                if a == 11 :
                    print("SKETCH PEN")
                if a == 13 :
                    print("GEL PEN")

print("Enter the number between 3 to 13")  
a = int(input("Enter an input number:"))  
if a >=3 and a <= 13 :
    PrimeChecker(a)