
num = 1;

for x in range(1,3):
    for y in range(1, 6):
        print(num, end=' '); # it gets a num = 6 if it reach a 2nd outer loop EX : 6 7 8 9 10
        num += 1;
    print("");

r = int(input("Enter the row number : "));
c = int(input("Enter the column number : "));

num = 1;
for x in range(1,r+1):
    for y in range(1, c+1):
        print(num, end=' '); 
        num += 1;
    print("");

num = 1;
for x in range(1,6):
    for y in range(1,x+1):
        print(y,"\t",end="");
    print("");



for x in range(1,6):
    for y in range(1,x+1):
        print(num,"\t",end="");
        num += 1;
    print("");