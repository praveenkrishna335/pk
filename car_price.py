car = int(input("Enter the no of cars : "))
onroad_tax = 0

for i in range(1, car + 1) :
    car_name = input("Enter the car name : ")
    car_price = int(input("Enter the car price : "))
    dis = int(input("Enter the discount : "))
    road_tax = int(input("Enter the road tax : "))

    if car_price < 500000 :
        gst = int((car_price * 8) / 100)
        print("The GST for car is : ", gst)
        onroad_tax = (car_price + road_tax + gst) - dis
        print("The ON ROAD TAX for the car is : ", onroad_tax)

    if (car_price >= 500000) and (car_price < 1000000) :
        gst = (car_price * 18) / 100
        print("The GST for car is : ", gst)
        onroad_tax = (car_price + road_tax + gst) - dis
        print("The ON ROAD TAX for the car is : ", onroad_tax)

    if car_price >= 1000000 :
        gst = (car_price * 28) / 100
        print("The GST for car is : ", gst)
        onroad_tax = (car_price + road_tax + gst) - dis
        print("The ON ROAD TAX for the car is : ", onroad_tax)
