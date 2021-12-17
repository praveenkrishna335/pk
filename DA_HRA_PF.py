id = input("Enter the employee id : ")
age = int(input("Enter the age : "))
salary = int(input("Enter the salary : "))

def sg5k() :
    def dearness() :
        da = (salary * 3) / 100
        print(da)
    def house() :
        hra = (salary * 5) / 100
        print(hra)
    def fund() :
        pf = (salary * 7) / 100
        print(pf)
        

def sg2k() :
    def dearness() :
        da = (salary * 5) / 100
    def house() :
        hra = (salary * 9) / 100
    def fund() :
        pf = (salary * 6) / 100

def sl2k() :
    def dearness() :
        da = (salary * 7) / 100
    def house() :
        hra = (salary * 95) / 100
    def fund() :
        pf = (salary * 5) / 100

if salary >= 50000 :
    sg5k()

elif salary <= 50000 and salary >= 20000 :
    sg2k()
else :
    sl2k()