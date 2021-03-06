# MATHEMATICAL FUNCTIONS

import math

# ceil(x)
print("***** The math ceil function *****")
print()
print(math.ceil(1.4))
print(math.ceil(1.1))
print(math.ceil(5.3))
print(math.ceil(-2.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))
print()
print("==============================")

# floor(x)
print("***** The math floor function *****")
print()
print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(-5.3))
print(math.floor(22.6))
print(math.floor(10.0))
print()
print("==============================")

# degrees(x) - converts radian into degree
print("***** The math degree function *****")
print()
print(math.degrees(8.90))
print(math.degrees(-20))
print(math.degrees(1))
print(math.degrees(90))
print()
print("==============================")

# radians(x)
print("***** The math radians function *****")
print()
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))
print()
print("==============================")

# sin(x)
print("***** The math sin function *****")
print()
print(math.sin(0.00))
print(math.sin(-1.23))
print(math.sin(10))
print(math.sin(math.pi))
print(math.sin(math.pi/2))
print(math.pi)
print()
print("==============================")

# cos(x)
print("***** The math cos function *****")
print()
print(math.cos(0.00))
print(math.cos(-1.23))
print(math.cos(10))
print(math.cos(3.14159687346))
print()
print("==============================")

# tan(x)
print("***** The math tan function *****")
print()
print(math.tan(90))
print(math.tan(-90))
print(math.tan(45))
print(math.tan(60))
print()
print("==============================")

# exp(x)
print("***** The math exp function *****")
print()
print(math.exp(65))
print(math.exp(-6.89))
print()
print("==============================")

# fabs(x)
print("***** The math fabs function *****")
print()
print(math.fabs(-66.43))
print(math.fabs(-7))
print(math.fabs(7))
print()
print("==============================")

# factorial(x)
print("***** The math factorial function *****")
print()
print(math.factorial(5))
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))
print()
print("==============================")

# fmod(x)
print("***** The math fmod function *****")
print()
print(math.fmod(20.36,4))
print(math.fmod(20,3))
print(math.fmod(15,6.369))
print(math.fmod(-10,3))
print()
print("==============================")

# fsum(x)
print("***** The math fsum function *****")
print()
print(math.fsum( (26.3, 5698.36) ))
print(math.fsum( [1, 2, 3, 4, 5] ))
print(math.fsum( [100, 400, 340, 500] ))
print()
print("==============================")

# log10(x)
print("***** The math log10 function *****")
print()
print(math.log10(2.35463))
print(math.log10(2))
print(math.log10(1))
print()
print("==============================")

# log(x, [,base]) -- This is ln()
print("***** The math natural log (ln) function *****")
print()
print(math.log(2.7183))
print(math.log(2, 10))
print(math.log(1))
print()
print("==============================")

# sqrt(x)
print("***** The math square root function *****")
print()
print(math.sqrt(49))
print(math.sqrt(9))
print(math.sqrt(25))
print(math.sqrt(16))
print(math.sqrt(15))
print()
print("==============================")

# pow(x,y)
print("***** The math power function *****")
print()
print(math.pow(5, 3))
print(math.pow(9, 3))
print(math.pow(2, 4))
print()
print("==============================")

# gcd(x, y)
print("***** The math gcd function *****")
print()
print(math.gcd(25, 30))
print(math.gcd(3, 6))
print(math.gcd(6, 12))
print(math.gcd(12, 36))
print(math.gcd(-12, -36))
print(math.gcd(5, 12))
print(math.gcd(10, 0))
print(math.gcd(0, 34))
print(math.gcd(0, 0))
print()
print("==============================")

# trunc(x)
print("***** The math trunc function *****")
print()
print(math.trunc(15.5676))
print(math.trunc(2.438676437327899034873))
print(math.trunc(8.24))
print(math.trunc(-99873727378.29))
print()
print("==============================")

# isinf(x) --- is infinite
print("***** The math isinf function *****")
print()
print(math.isinf (56) )
print(math.isinf (-45.34) )
print(math.isinf (+45.34) )
print(math.isinf (math.inf) )
print(math.isinf (float("nan")) )
print(math.isinf (float("inf")) )
print(math.isinf (float("-inf")) )
print(math.isinf (-math.inf) )
print()
print("==============================")

# isnan(x) ---- is number
print("***** The math isnan function *****")
print()
print(math.isnan (56) )
print(math.isnan (-45.34) )
print(math.isnan (+45.34) )
print(math.isnan (math.inf) )
print(math.isnan (float("nan")) )
print(math.isnan (float("inf")) )
print(math.isnan (float("-inf")) )
print(math.isnan (math.nan) )
print()
print("==============================")

# Constants in math module
print("***** The math constants function *****")
print()
print("The value of pi is: ", math.pi)
print("The value of e is: ", math.e)
print("The value of inf is: ", math.inf)
print("The value of nan is: ", math.nan)
print("The value of tau is: ", math.tau)
print()
print("==============================")
