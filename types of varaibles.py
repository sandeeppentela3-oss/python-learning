#local varaible 
def greet():
    name = "Sandeep"  # Local variable
    print(name)

greet()

#global varaible 
college = "ABC College"  # Global variable

def show():
    print(college)

show()
print(college)

#instance varaible

class Student:
    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Sandeep")
print(s1.name)

#class varaible
class Student:
    college = "ABC College"  # Class variable

s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)