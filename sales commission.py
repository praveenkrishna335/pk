# name = input("Enter the sales executor name : ");
# # sc - sales commission
# sc = int(input("Enter the sales commission : "));

# if (sc <= 50000):
#     a = (sc*1)/100;
#     print("The commission for sales executor is : ",a);
# elif (sc > 50000 and sc < 100000):
#     b = (sc*2)/100;
#     print("The commission for sales executor is : ",b);
# else :
#     c = (sc*3)/100;
#     print("The commission for sales executor is : ");


name = input("Enter the sales executor name : ");
# sc - sales commission
sc = int(input("Enter the sales commission : "));

if (sc <= 50000):
    a = (sc*1)/100;
    
elif (sc > 50000 and sc < 100000):
    a = (sc*2)/100;
    
else :
    a = (sc*3)/100;
print("The commission for sales executor is : ", int(a));