import sys

print("***********************\n1 . GET DETAILS\n2 . RESULTS\n3 . EXIT\n***********************")

choice = int(input("Enter your choice : "))

if choice == 1 :
    reg_no = int(input("Enter student reg no : "))
    name = input("Enter your name : ")
    marks_1 = int(input("Enter student marks 1 : "))
    marks_2 = int(input("Enter student marks 2 : "))

if (marks_1 >= 0 and marks_1 <= 100) and (marks_2 >= 0 and marks_2 <= 100) :
    choice = int(input("Enter your choice : "))

    if choice == 2 :
        total = marks_1 + marks_2
        print("The total marks is : ", total)
        avg = total / 2
        print("The average is : ", avg)
        if marks_1 < 35 or marks_2 < 35 :
            print("FAIL")
        if avg >= 35 and avg <=80 :
            print("PASS")
        if avg > 80 and avg <= 100 :
            print("EXCELLENT")
else :
    print("Please enter a marks between 1 to 100")
    sys.exit()

choice = int(input("Enter your choice : "))

if choice == 3 :
    sys.exit()

if (choice != 1 and choice != 2 and choice != 3) :
    print("Please enter a correct choice")