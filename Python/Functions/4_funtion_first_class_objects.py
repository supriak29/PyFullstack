# Functions are First Class Objects:

# 1. it is possible to assign a function to a variable
# 2. it is possible to define one function inside another function
# 3. it is possible to pass a function as parameter to another function
# 4. it is possible that a function can return another function

#############################################

# assign a function to a variable
def display(str):
    return "Hi! " + str

#calling a function & assigning it function to variable x
x = display("Supriya")
print(x)
print()
print(30*"-")

#############################################

# define a function inside another function
def display(str):

    def message():
        return "How are you "

    result = message() + str + " ?"
    return result

#calling the function
print(display("Supriya"))

print()
print(30*"-")
    
#############################################

# Function can return another function
def addition():
    
    def multiplication():
        print("Multiplication: ")
        return 10*20
    def movie():
        print("This is a movie name")
        return "Superman"
    
    return multiplication, movie

a,b = addition()
print(a(),"\n")
print(b(),"\n")

# result = addition()
# print(result)

print(30*"-")

#############################################

# function can be passed as parameters to other functions

# Funct 1:
def addition(fun):
    c = 10 + fun
    return c
##  return 'Hi' + fun

# Funct 2:
def number():
    return 100
#   return "How are you?"

# calling display() function & pass number() function
print("Result using Nested Function: ",addition(number()))
print()
print(30*"-")

##############################################
