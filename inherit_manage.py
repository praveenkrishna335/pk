class management:
    print("NPR GROUP OF INSTITUTIONS")
    
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
        print("management running")

class principal(management):
    def __init__(self,name,dept,year,ident):
        self.year = year
        self.ident = ident
        management.__init__(self, name, dept)

class staff(principal):
    def __init__(self,name,dept,year,ident,mentor):
        self.mentor = mentor
        principal.__init__(self,name,dept,year,ident)

s1 = staff('pk','ECE',2020,26,'sabarish')
print(s1.name)
print(s1.mentor)
print(s1.year)
print(s1.dept)
print(s1.ident)