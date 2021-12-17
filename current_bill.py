id = int(input("Enter your customer id : "))
pre = int(input("Enter the previous unit : "))
curr = int(input("Enter the previous unit : "))

print("***************\n1 . DOMESTIC\n2 . COMMERCIAL\n3 . INDUSTRY\n***************")
choice = int(input("Do you want to continue, press '1' : "))
cat = int(input("Enter your catagory : "))

unit = curr - pre

if choice == 1 :
    if cat == 1 :
        if unit >= 0 and unit <= 100 :
            bill = unit * 2.75
            print("The current bil for the month is : {} RS")
        if unit >= 101 and unit <=500 :
            bill = unit * 4.50
            print("The current bil for the month is : {} RS")
        if unit >= 500 :
            bill = unit * 5
            print("The current bil for the month is : {} RS")
    if cat == 2 :
        if unit >=  0 and unit <= 200 :
            bill = unit * 5
            print("The current bil for the month is : {} RS")
        if unit >= 201 and unit <=500 :
            bill = unit * 5.5
            print("The current bil for the month is : {} RS")
        if unit >= 500 :
            bill = unit * 6
            print("The current bil for the month is : {} RS")
    if cat == 3 :
        if unit >= 0 :
            bill = unit * 10
            print("The current bil for the month is : {} RS")
