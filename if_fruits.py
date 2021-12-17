cname = input("enter your name : ");
print("*****COST OF JUICES*****");
print("Orange = 40  Apple = 50  Pinnapple = 25");
j = input("which juice do you want : ");

if (j == 'orange'):
    qty = int(input("how many Orange juice do you want : "));
    price = print("Total amount payable : ", 40 * qty, "RS");
if (j == 'apple'):
    qty = int(input("how many Apple juice do you want : "));
    price = print("Total amount payable : ", 50 * qty, "RS");
if (j == 'pinnapple'):
    qty = int(input("how many Pinnapple juice do you want : "));
    price = print("Total amount payable : ", 25 * qty, "RS");