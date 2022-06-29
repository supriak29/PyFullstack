# INSERT
# COPY

# list.insert(i, x) ---> i=index, x=value

# to add particular value to a particular index

new = [0,1,2,3,4]
print(new)
new.insert(2,"Start")
print("After insertion: ",new)

print()

#list.copy()

# to copy all the list elements into new list and return it

latest = new.copy()
print("Latest List: ",latest)
