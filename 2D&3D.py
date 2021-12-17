import math
def circle(o):
    area_o = math.pi * (o ** 2)
    print("The area of the CIRCLE is : ", area_o)
def trapezium(b1,b2,h):
    area_t = ( (b1 + b2) * h ) / 2
    print("The area of the TRAPEZIUM is : ", area_t)
def cylinder(r,h):
    area_c = ( (2 * r * h) * math.pi ) + ( math.pi * 2 * (r ** 2) )
    print("The area of the CYLINDER is : ", area_c)
def sphere(r):
    area_s = math.pi * 4 * (r ** 2)
    print("The area of the SPHERE is : ", area_s)

print("********************\n 1 . 2D OBJECTS \n   1 . CIRCLE \n   2 . TRAPEZIUM \n\n 2 . 3D OBJECTS \n   1 . CYLINDER \n   2 . SPHERE \n********************")

choice = int(input("Enter your choice : "))
if choice == 1 :
    print("********2D OBJECTS********")
    D2 = int(input("Which 2D print do you want : "))

    if D2 == 1 :
        print("********CIRCLE********")
        o = int(input("Enter the r value : "))
        circle(o)

    if D2 == 2 :
        print("********TRAPEZIUM********")
        b1 = int(input("Enter the B1 value : "))
        b2 = int(input("Enter the B2 value : "))
        h = int(input("Enter the H value : "))
        trapezium(b1, b2, h)

if choice == 2 :
    print("********3D OBJECTS********")
    D3 = int(input("Which 3D print do you want : "))

    if D3 == 1 :
        print("********CYLINDER********")
        r = int(input("Enter the R value : "))
        h = int(input("Enter the H value : "))
        cylinder(r, h)

    if D3 == 2 :
        print("********SPHERE********")
        r = int(input("Enter the R value : "))
        sphere(r)