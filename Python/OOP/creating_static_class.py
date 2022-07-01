# STATIC CLASS creation

class Student:
    '''Static class of student'''

    # Below block defines attributes of Student
    def __init__(self):
        self.name = "Supriya"
        self.age = 21
        self.marks = 900

    # below block defines methods
    def talk(self):
        print("Hi, I am ",self.name)
        print("My age is ",self.age)
        print("My marks are ",self.marks)


# creating objects a & abc of class Student
a = Student()
abc = Student()

# memory location assigned to Student object
print("Id of object a: ",id(a))
print()

# memory location assigned to a.talk() object
print("Id of a.talk(): ",id(a.talk))

print()

##
# To print variables & it's memory location
print("Accessing class attribute(name) through object: ",a.name) 
print("Id of a.name: ",id(a.name))
print()

print("Accessing class attribute(age) through object: ",a.age) 
print("Id of a.age: ",id(a.age))

print()

print("Marks: ",a.marks)
print("Id of a.marks: ",id(a.marks))

print()

# calls talk() function of Student class
a.talk()
