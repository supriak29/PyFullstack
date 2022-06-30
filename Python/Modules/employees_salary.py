# from employees import da, hra, pf, itax
from employees import *

# using employee module to calculate gross & net
# salary of an employee

# calculate gross salary of employee by taking basic

basic = float(input("Enter basic salary: "))

# calculate the gross salary
gross = basic + da(basic) + hra(basic)

da(1000)
print("Your gross salary: {}".format(gross))
print(__name__)

# calculate net salary
net = gross - pf(basic) - itax(gross)
print("Your net salary is: {}".format(net))
