# Python program to create a student class with a constructor having more than one parameter

class Student:
    '''Dynamic'''
    # this is a constructor
    def __init__(self,n=' ',m=0):   # passing default values
        self.name = n
        self.marks = m

    # this is an instance method
    def display(self):
        print("Hi, ",self.name)
        print("Your marks: ",self.marks)

# constructor called without any arguments
s = Student(n="Supriya",m=100)
s.display()

print("-"*30)

def check_input(marks):
    if marks == '':
        marks = 0
    return marks

# constructor called with 2 args
name = input("Enter your name: ")
marks = check_input(int(input("Enter your marks: ")))

s1 = Student(name,marks)
s1.display()
print("-"*30)
