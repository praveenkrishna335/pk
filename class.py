# class Person:
#     def __init__(self,name,age):
#         self.fname = name
#         self.per_age = age
# p1 = Person("pk",23)
# print(p1.fname)
# print(p1.per_age)

# class Person:
#     def __init__(self,name,age):
#         self.fname = name
#         self.per_age = age

#     def myfunc(self):
#         print("The username is : ",self.fname)
# p1 = Person("pk",23)

# print(p1.fname)
# print(p1.per_age)
# p1.myfunc()

class Person:
    def __init__(self,name,age):
        self.fname = name
        self.per_age = age
    
    def myfunc(whatever):
        print("The username is : "+ whatever.fname)

name1 = input("Enter your name : ")
age1 = int(input("Enter your age : "))
p1 = Person(name1,age1)

print(p1.fname)
print(p1.per_age)
p1.myfunc()