class base (object) :
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

class child (base):
    def __init__(self,name,age):
        base.__init__(self, name)
        self.age = age
    def getAge(self):
        return self.age
    
class grandChild(child):
    def __init__(self,name,age,address):
        child.__init__(self, name, age)
        self.address = address
    def getAddress(self):
        return self.address

g = grandChild("pk", 23, "Madurai")

print(g.getName(),g.getAge(),g.getAddress())