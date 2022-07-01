# Types of methods

# 1. Instance Method
#       (a) Accessor method
#       (b) Mutator method
# 2. Class method
# 3. Static method

############################################

# Instance method to process data of the objects
class Student:
    ''' '''
    # constructor
    def __init__(self, n=' ', m=0):
        self.name = n   # instance variable
        self.marks = m  # instance variable

    # Instance method & Accessor method
    def display(self):
        print("Hi, my name is ", self.name)
        print("My marks are ",self.marks)

    # to calculate grades based on marks is also an instance method
    # this is a mutator method
    def calculate(self):
        if (self.marks >= 600):
            print("You got first grade")
        elif (self.marks >= 500):
            print("You got second grade")
        elif (self.marks >= 350):
            print("You got third grade")
        else:
            print("Better luck next time")
        print()

    # create instance with some data from keyboard
    # n = int(input("How many students?"))

name = input("Enter name: ")
marks = int(input("Enter marks: "))

print()

# create student class instance & store data
s = Student(name, marks)
s.display()
s.calculate()
    
#######################################################

# Python prog. to use method to handle common features of all instances

# understanding class methods
class Bird:
    ''' '''
    # this is a class variable
    wings = 2

    # this is a class method
    @classmethod
    def fly(cls, name):
        print(f'{name} files with {Bird.wings} wings')
#       print('{} flies with {} wings'.format(name,cls.wings))

# to display information for 2 birds
Bird.fly("Sparrow")
Bird.fly("Crow")

print()

##########################################################

# Python prog. to create a static method that counts the number of instances

# Static methods
class Myclass:
    # class/static variable
    n = 10

    # constuctor that increments n when an instance is created
    def __init__(self):
        Myclass.n = Myclass.n+1     # a = a+1

#   def variable_class(cls):
#       print(cls.n)

    # this is a static method to display no. of instances
    @staticmethod
    def noObjects():
        print(f'Np. of instances created: {Myclass.n}')


# created 3 instances
obj1 = Myclass()
Myclass.noObjects()

obj2 = Myclass()
Myclass.noObjects()

obj3 = Myclass()
Myclass.noObjects()
