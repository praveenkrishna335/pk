# For one condition is satisfied
name = input("Enter your name : ");
age = int(input("Enter your age : "));
gender = input("Enter your gender : ");
degree = input("Enter your degree : ");
exp = int(input("Enter your experience : "));
district = input("Enter your district : ");

if (degree == "be" and exp >= 1 and age >= 18):
    print("yoy are qualified for this position");
elif (degree != "be" and exp >= 1 and age >= 18):
    print("You are not qualified because of degree");
elif (degree == "be" and exp < 1 and age >= 18):
    print("You are not qualified because of experience");
else:
    print("You are not qualified because of age");
# End of program

