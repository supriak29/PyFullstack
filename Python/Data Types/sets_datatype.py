# Example of sets in python

# 1. starts with curly bracktes
# 2. all datatypes can be included
# 3. no repetation of elements in set
# 4. randomly arranged elements at output

############################################################



# creating sets with repeated values
my_set = {1, 2,2,2,2,2,2, 1,5,5.5,5.1,2, 'Hello','123','Happy','123'}
print('This is my set: ',my_set,'\n') # prints the values only once even if they are repeated while declaring a set

#This will give error, as indexing is not supported in set
## my_set[0] = 25

print('This is the type of set: ',type(my_set),'\n') #printing the datatype

# adding an individual element in set
# the elements gets added anywhere in the set, there is no particular position as indexing is not supported
my_set.add(55)
my_set.add('This is the example')
print(my_set)
print(type(my_set))


#removing an element from set
my_set.remove('Hello')
print(my_set)
print(type(my_set))
