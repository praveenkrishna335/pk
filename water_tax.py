print("**************************\n\n      1 LITRE = 0.01094 RS\n   1000 LITRE = 10.94   RS\n\n**************************")

id = int(input("Enter your consumer id : "))
list1 = []
list1.append(id)
name = input("Enter your name : ")
list2 = []
list2.append(name)
addr = input("Enter your address : ")
list3 = []
list3.append(addr)
usage = int(input("Enter the water usage : "))
list4 = []
list4.append(usage)
bill = usage * 0.01094
list5 = []
list5.append(bill)

print("*****************************************************************************************\n CONSUMER ID      NAME             ADDRESS                WATER USAGE         BILL AMOUNT \n*****************************************************************************************")

for i,j,k,l,m in zip(list1,list2,list3,list4,list5) :
    print(i,"\t\t",j,"\t\t",k,"\t\t",l,"\t\t",m)

print("*****************************************************************************************")