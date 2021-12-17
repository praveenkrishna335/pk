id = input("Enter the employee id : ")
age = int(input("Enter the age : "))
salary = int(input("Enter the salary : "))

def sg5k() :
    da = (salary * 3) / 100
    hra = (salary * 5) / 100
    pf = (salary * 7) / 100
    print("The DA is : ", da)
    print("The HRA is : ", hra)
    print("The PF is : ", pf)
    gs = salary + da + hra
    print("The GROSS SALARY is : ", gs)
    ns = gs - pf
    print("The NET SALARY is : ", ns)
        
def sg2k() :
    da = (salary * 5) / 100
    hra = (salary * 9) / 100
    pf = (salary * 6) / 100
    print("The DA is : ", da)
    print("The HRA is : ", hra)
    print("The PF is : ", pf)
    gs = salary + da + hra
    print("The GROSS SALARY is : ", gs)
    ns = gs - pf
    print("The NET SALARY is : ", ns)

def sl2k() :
    da = (salary * 7) / 100
    hra = (salary * 95) / 100
    pf = (salary * 5) / 100
    print("The DA is : ", da)
    print("The HRA is : ", hra)
    print("The PF is : ", pf)
    gs = salary + da + hra
    print("The GROSS SALARY is : ", gs)
    ns = gs - pf
    print("The NET SALARY is : ", ns)

if salary >= 50000 :
    sg5k()

elif salary <= 50000 and salary >= 20000 :
    sg2k()
else :
    sl2k()