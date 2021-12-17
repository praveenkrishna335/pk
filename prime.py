def PrimeChecker(a):  
  
    if a > 1:  
        for j in range(2, int(a/2) + 1):  
            if (a % j) != 0:
                print("{} is a prime number".format(j))
            else :
                print("{} is not a prime number".format(j))
        
a = int(input("Enter an input number:"))  

PrimeChecker(a)