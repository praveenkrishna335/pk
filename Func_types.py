#function calling...
def add() :
    a = int(input("Enter the 1st number : "));
    b = int(input("Enter the 2nd number : "));
    c = a + b;
    print("The sum is : ", c);
add();

#call by value...
def add(a, b) :
    c = a + b;
    print("The sum is : ", c);
add(5,5);


def add(a = 5, b = 5) :
    c = a + b;
    print("The sum is : ", c);
add();
