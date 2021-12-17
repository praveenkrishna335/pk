name = input("Enter your name : ");
age = int(input("Enter your age : "));

if (age >= 18):
    print("You have required age");
    degree = input("Enter your degree : ");
    if (degree == "be"):
        print("You have required degree");
        exp = int(input("Enter your experience : "));
        if (exp >= 1):
            print("You have required experience");
            print("You are qualified for this position");
        else:
            print("You are not qualified because of experience");
    else:
        print("You are not qualified because of degree");
else:
    print("You are not qualified because of age");