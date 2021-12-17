n1 = int(input("Enter the 1st number : "));
n2 = int(input("Enter the 2nd number : "));

if n1 != n2 :
    if n1 > n2 :
        n1 -= n2;
        print("The G.C.D of the two number is : ", n1);
    else :
        n2 -= n1;
        print("The G.C.D of the two number is : ", n2);