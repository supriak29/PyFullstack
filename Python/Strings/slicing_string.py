# SLICING STRING

# string[start:stop-1:stepsize]

name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(name)
print(len(name))
print()

b = name[0:8:1]
print(b)
print(len(b))
print()

c = b[0:5]
print(c)
print(len(c))
print()

b = name[0:8]
print(b)
print(name[:10])
print(name[8::])

########################################

# start=?, stop=?, stepsize=?, blank=___
# name[start::]
# name[:stop:]
# name[start:stop]
# name[start::2]

#########################################

# Negative indexing

name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# access from name[-4] to name[-2] from left to right in name
print(name[-4:-1])
print()

print(name[-5:-2])
print()
### retrive the name string from first to last from right to left
print(name[-1::])
print(name[-1])
print(name[::-1])
