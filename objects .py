class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
student1 = Student("Sandeep", 22)
student2 = Student("Rahul", 21)

# Calling methods using objects
student1.display()
print("----------")
student2.display()