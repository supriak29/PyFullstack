# LIST

# 1. example for creating list
# 2. list can hold multiple datatypes
# 3. indexing can be done
# 4. mutable

#############################################

# creating a list with []
a = []
print(type(a))
print("This is an empty list: ",a)

# creating list with various datatypes
new_list = [1, 2, 25, 53.44, "ABC", 3+5j]
print(type(new_list))

# to check the mutability of list
print(new_list[2])
print(type(new_list[2]))

#modify the element in the list
new_list[0] = 10000000000
print(new_list)

# using reverse indexing
print(new_list[-1])
print(new_list[5])
print(new_list[-2])
