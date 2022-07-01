# Types of Variables in class

# 1. Instance Variables
# 2. Class Variables or Static Variables

print("Instance Variable example\n")
# instance variable example
class Sample:
    '''This is a simple example of instance variable'''
    # this is a constructor
    def __init__(self):
        self.x = 10 # instance variable

    # this is a instance method
    def modify(self):
        self.x += 1

print("***** Object 1 *****\n")
a = Sample()
print("Instance Varible: ",a.x)
a.modify()
print("After modify: ",a.x)
print("-"*30)

print("\n***** Object 2 *****\n")
b = Sample()
print("Instance Variable: ",b.x)
print("-"*30,"\n")
# create 2 instance
s1 = Sample() # 10
s2 = Sample() # 10

s1.modify() # 11
s1.modify() # 12
s1.modify() # 13
print("x in s1: ",s1.x) # 13
print("x in s2: ",s2.x) # 10, since s2 is not modified yet.
##
print("\n","-"*30,"\n")

##########################################
print("Class variables or Static Variables Examples")

# Class variables or Static Variables

class Sample:
    # class var or static var
    x = 10      

    # class method
    @classmethod
    def modify(cls):
        cls.x += 1

# create 2 instances
s1 = Sample()
s2 = Sample()

print("x in s1 = ",s1.x)
print("x in s2 = ",s2.x)

print("\n","-"*30,"\n")

# modify x in s1 only
s1.modify()
s1.modify()
s1.modify()
print("x in s1 = ",s1.x)
print("x in s1 = ",s2.x)
