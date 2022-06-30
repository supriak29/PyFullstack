# LOCAL variable in a function
print("\nLOCAL variable\n")

def myfunct():
    a = 1 # this is a local variable
    a += 1 # increment it
    print("This is 'a' inside the function: ",a) # display

# calling myfunct()
myfunct()
# print(a) # local variable has limited scope & can't be used outside that function

print()
print("-"*30)
print()

##############################################

# GLOBAL variable
print("GLOBAL variable\n")

a = 1 # this is a global variable
def myfunct():
    b = 2 #this is a local variable
    print("Printing value of 'a', global variable from within the funct: ",a,"\n") #display global variable
    print("'b', local variable inside funct: ",b,"\n") # display local variable

print()
myfunct()
print("Print global variable from outside funct, a: ",a,"\n")
#print(b) #error, not available

print()
print("-"*30)
print()

##############################################

# Same name for local & global variable
print("Same name for local & global variable\n")

a = 11 # global
def myfunct():
    a = 2 # local
    print("Inside funct: ",a) # displays local

myfunct()
print("Outside function: ",a) # displays global

print()
print("-"*30)
print()

##############################################

# GLOBAL KEYWORD - modify global variable

# program to access the global variable inside function
# and modify it

print("GLOBAL KEYWORD\n")

a = 10 # global variable
print("This is 1st time, global a: ",a)

def myfunct():
    global a # this is global variable
    print("Global a: ",a)

    a = 2 # modified the global variable
    print("Modified a: ",a) # display new value

# calling function
myfunct()
print("This is 2nd time global, after modification a: ",a) #display modified value

print()
print("-"*30)
print()

##############################################

# Same name for global & local variable
print("Same name for global & local variable \n")

a = 10 # global
def myfunct():
    a = 2               # local
    x = globals()['a']  # get global into x
    print("Global variable a as x: ",x)
    print("Local variable a: ",a)

myfunct()
print("Global Variable a: ",a)

print()
print("-"*30)
print()
