# 2. Function - return

def sum(a,b):
    '''This function adds two numbers and returns value'''
    c = a+b
    return c

#function calling
r = sum(100,50)
print("Add: r = 100 + 50 = ",r)
print()

# example 1
if r >= 100:
    r -=100
    print("Result: r - 100 = ",r)
print()

#example 2
x = sum(10,20)
multiply = x*10
print("This is x: ",x)
print()
print("Multiply: x * 10 = ",multiply)
