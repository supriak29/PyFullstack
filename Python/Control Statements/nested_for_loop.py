# Start Pattern in rigth angled triangle

# range(start, stop-1, step)

#   *
#   **
#   ***
#   ****
#   *****
#   ******
#   *******
#   ********
#   *********
#   **********

for i in range(1,11):
    for j in range(1,i+1):
        print('*',end='')
    print()


print()
print("==========================")
print()

# display numbers from 1-100 in 10 rows & 10 cols

for x in range(1,11):
    for y in range(1,11):
        print("{}".format(x*y),end='\t')
    print()


print()
print("==========================")
print()

#################
# use of end=''

print("Python",end=',')
print("Java",end=',')
print("C++",end=".")
print("JavaScript")
print("HTML")
