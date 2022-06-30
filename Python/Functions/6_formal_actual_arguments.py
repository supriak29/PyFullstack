# FORMAL & ACTUAL arguments

# This is Actual Arguments used in a function call are of 4 types:
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable Length Arguments
# 5. Variable Length Arguments using 

###############################################

# 1. Positional Arguments
print("1. Positional Arguments \n")
def attach(s1, s2):
    '''To join s1 and s2 & display total string'''
    s3 = s1 + s2
    print(s3)

# call attach() & pass 2 strings
attach("New", "York")
attach("York", "New")

print()
print(30*"-")
print()

#############################################

# 2. Keywords Arguments
print("2. Keywords Arguments \n")

def grocery(product,price):
    '''To display the given arguments'''
    print("Product: ",product)
    print("Price: ",price)

# call the grocery() function & pass 2 arguments
# grocery(100,"Sugar")
grocery(price=100,product="Sugar")

print()
print(30*"-")
print()

#############################################

# 3. Default Arguments
print("3. Default Arguments \n")

def grocery(product, price=40.0):
    '''To display the given arguments'''
    print("Product: ",product)
    print("Price: ",price)

# call the grocery() function& pass arguments
grocery(price=45.0,product="Sugar")
grocery(product="Sugar")

print()
print(30*"-")
print()

#############################################

# 4.1. Variable Length Arguments
print("4. Variable Length Arguments \n")

def add(abc, *args): # (50) - [1 arg], (10,20,30,40,50) - [5 args]
    '''to add given numbers'''
    print("Formal Arguments: ",abc)

    sum = 0
    for i in args: # 5 args are there
        sum += 1 # 0+1+1+1+1+1 = 5
    print("Sum of all nos. + Formal Arg = ",(abc + sum)) # 5 + 50 = 55

# calling add() function & pass args
## add(5, 10)
add(50, 10,20,30,40,50) # here, 50 is the formal arg & rest are actual

print()
print(30*"-")
print()

#############################################

# 5. Varible Length Argument using dictionary
print("5. Varible Length Argument using dictionary \n")

def display(farg, **kwargs):
    """to display given values"""
    print("Formal Args: ",farg)

    for x,y in kwargs.items():
        print(f"Key = {x}, Value = {y}")

# calling the function
## display(5, rno = 10)
print()

display(5, rno=1, name="Supriya")

print()
print(30*"-")
print()

#############################################

