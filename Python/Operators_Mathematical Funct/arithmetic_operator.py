# ARITHMETIC OPERATORS

# let's assign some values to variables
a = 13
b= 5
## a, b = 13, 5

##############################################

#addition operator
c = a+b
print("Addition of 'a' and 'b': ",c)
print("This is the identity of c: ",id(c))
print("Addition of 'a' and 'b': ",a+b)
print("This is the identity of a+b: ",id(a+b),"\n")

#subtraction operator
c = a-b
print("Subtraction of 'a' and 'b': ",c)
print("This is the identity of c: ",id(c))
print("Subtracting 'b' from 'a' gives: ",a-b)
print("This is the identity of a-b: ",id(a-b),"\n")

#multiplication operator
c = a*b
print("Multiplication of 'a' and 'b': ",c)
print("This is the identity of c: ",id(c))
print("Multiplication of 'a' and 'b': ",a*b)
print("This is the identity of a*b: ",id(a*b),"\n")

#division operator
print("The value of a: ",a)
print("The value of b: ",b)
print("Division of 'a' by 'b': ",a/b,"\n")

#modulus operator
print("The value of a: ",a)
print("The value of b: ",b)
print("Modulus of 'a' by 'b' gives remainder: ",a%b,"\n")

#exponential operator
print("The value of a: ",a)
print("The value of b: ",b)
print("Exponent of 'a' to the power of 'b' is: ",a**b,"\n")

#Integer division operator
print("The value of a: ",a)
print("The value of b: ",b)
print("Integer Division of 'a' by 'b' gives integer value of quotent: ",a//b,"\n")

############################

#Order of Evaluation

x = 1; y = 2; z = 3; a = 2; b = 2; c = 3
result = (x+y)*z**a//b+c
print("The answer for order of evaluation is: ", result)
