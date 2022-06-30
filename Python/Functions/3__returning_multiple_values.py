# returning MULTIPLE values from a function

# Function defination
def solve(a,b):
    '''docstring'''
    c = a + b
    d = a - b
    z = a * b
    return c, d, z

# calling function

# Method 1:
p,q,r = solve(10,20)
print(p,q,r, sep=', ')

# Method 2:
# defining variable
a = 50
b = 100

p,q,r = solve(a,b)
print(p,q,r, sep=', ')

# Method 3:
# this will give the tuple with 2 elements
# Here, tuple is created automatically
# Assigning a function to a varible by calling a function
x = solve(a,b)
print(x)
