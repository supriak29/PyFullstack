# decorators in functions

def decor(fun):     # gift wrapping

    def inner():
        value = fun()   # access value returned by fun()
        return value + 2 # increase the value by 2
    return inner

@decor
def num():
    return 10

print("Print using decorator: ",num())

print("\n",30*"-","\n")

########################

# calling decorator function using '@' method
def decor_two(fun):

    def inner():
        value = fun()   # access value returned by fun()
        return value + 2 # increase value by 2
    return inner    # return inner function

# calling decorator funct using '@' method
def decor_eight(fun):

    def inner():
        value = fun()   # access value returned by fun()
        return value + 8 # increase value by 8
    return inner    # return inner function

# take a function to which decorator should be applied
@decor_two
@decor_eight
def num():
    '''some statements process'''
    return 10

# call decorator function & pass num
print(num()) # call result_fun & display the result

print("\n",30*"-","\n")

#################################
