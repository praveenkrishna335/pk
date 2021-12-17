hard = int(input("Enter the hardness of the steel : "))
carbon = float(input("Enter the carbon of the steel : "))
tensile = int(input("Enter the tensile the steel : "))

if hard > 25 and carbon < 0.7 and tensile > 6500 :
    print("\"10\" GRADE")
elif hard > 25 and carbon < 0.7 :
    print("\"9\" GRADE")
elif carbon < 0.7 and tensile > 6500 :
    print("\"8\" GRADE")
elif hard > 25 and tensile > 6500 :
    print("\"7\" GRADE")
elif hard > 25 or carbon < 0.7 or tensile > 6500 :
    print("\"6\" GRADE")
else :
    print("\"5\" GRADE")