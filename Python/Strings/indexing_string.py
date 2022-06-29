# INDEXING in python

address = "Thane West, near Thane station near McDonalds"
print(len(address))
print()
print(address[0])
print()
print(address[1])
print()
print(address[-1])
print()

add = "Python"
print(add[0])
print(len(add))
print(add)

# This will give IndexError
print(add[7])
print(add[8])

# This will give error, as strings are immutable
## add[0] = 'K'
add = "Python"
# this will not get printed as we got error above
print(add)
