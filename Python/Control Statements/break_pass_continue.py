# using break to come out of while loop

print("Break")
print()
x = 10
while x >= 1:
    x -= 1
    if x==5:
        break
    print("x:",x)
print("out of the loop")

print()
print("===============================")
print("Pass")
print()

#########################################

# pass

x = 10
while x >= 1:
    x -= 1
    if x==5:
        pass
    print("x:",x)
print("out of the loop")

print()
print("===============================")
print("Continue")
print()

###########################################

# continue
x = 10
while x >= 1:
    x -= 1
    if x==5:
        continue
    print("x:",x)
print("out of the loop")
