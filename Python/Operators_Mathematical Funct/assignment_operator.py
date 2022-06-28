# ASSIGNMENT OPERATOR

## x=20
## y=10
## z=5

# Different Assigning methods
## x,y,z = 20,10,5

# Adding assignment operator
x,y,z = 20,10,5
print("x = ",x)
print("x identity: ",id(x))
print("y = ",y)
print("y identity: ",id(y))
print("z = ",z)
print("z identity: ",id(z))
print()

z+=x
print("z identity: ",id(z))
print("Addition: Will add x and z and will store it's result in z: ",z)
print()

# Subtraction Assignment operator
x,y,z = 20,10,5
z-=x
print("Subtraction: Will subtract z from x and will store it's result in z: ",z)
print()

# Multiplication Assignment operator
x,y,z = 20,10,5
z*=x
print("Multiplication: Will multiply x with z and will store it's result in z: ",z)
print()

# Division Assignment operator
x,y,z = 20,10,5
z/=x
print("Division: Will divide z by x and will store it's result in z: ",z)
print()

# Modulus Assignment operator
x,y,z = 20,10,5
z%=x
print("Modulus: Will divide z by x and will store it's result in z: ",z)
print()

# Exponential Assignment operator
x,y,z = 20,10,5
z**=y
print("Exponential: Will perform power value of y for z and will store it's result in z: ",z)
print()

# Floor Division Assignment operator
x,y,z = 20,10,5
z//=x
print("Floor Division: Will perform floor division and will store it's result in z: ",z)

