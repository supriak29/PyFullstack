### Anonymous Functions or Lambdas
##
### lambda variables:expression
##
##########################################
##
###1. procedural way
##x = 5
##y = 5
##z = x+y
##print(z)
##
##print("\n",30*"-","\n")
##
############################################
##
###2. using Function
##def sum(x,y):
##    z = x+y
##    print(z)
##
##sum(5,5)
##
##print("\n",30*"-","\n")
##
############################################
##
###3. using lambda
##f = lambda x,y,z:(x+y)*z
##value = f(5,5,2)
##print(value)
##
##print("\n",30*"-","\n")
##
#######################
##
### lambda to calculate multiplication of values
##f = lambda x,y,z:x*y*z
##value = f(5,5,10)
##print("Multiplication: ",value)
##
##print("\n",30*"-","\n")
##
##########################
##
### lambda to find bigger number
##maxx = lambda x,y: x if x>y else y
##a,b = [int(n) for n in input("Enter 2 nos.: ").split()]
##print("Bigger no. is: ", maxx(a,b))
##
##print("\n",30*"-","\n")
##
##########################
##
### using lambdas with filter() function
### filter(function,sequence)
##
### using filter() funct filter put the even nos. from a list
####def is_even(x):
####    '''Doc string s'''
##
##########################
##
### map() 
### map(function, sequence)
##print("Map function:\n")
### map() function that gives squares
##def square(x):
##    ''''''
##    return x*x


###########################

# let us take a list of numbers
lst = [146,3154,6184,611,4,10]

### call map() with square() & lst
##lst1 = list(map(square,lst))
##print(lst1)

print("\nMap with lambda 1:\n")
lst1 = list(map(lambda x:x*x,lst))
print(lst1)

print("\nMap with lambda 2:\n")
lst1 = list(map(lambda x:x,lst))
print(lst1)

print("\n",30*"-","\n")

############################

### reduce()
### reduce(function,sequence)
##from functools import *
##lst = [1,2,3,4,5,6]
##result = 
