# DICTIONARY METHODS

detail = {"Name":"Supriya",
          "Location":"Dahisar",
          "Mobile":"9867254717",
          "Coding":"Python"}

print("ORIGINAL DICTIONARY: \n",detail)
print()

# dict.values() to get all the values from the dictionary
a = list(detail.values())
print(a)
print(type(detail.values()))

print("="*50)
print()

# dict.keys() to get all the keys from dictionary
b = list(detail.keys())
print(b)
print(type(detail.keys()))

print("="*50)
print()

# dict.update() to add new key-value pair to the dictionary
print("Dictionary after update: \n")
detail.update({"Surname":"Karkera"})
print(detail)

print("="*50)
print()

# dict.setdefault() returns a value of the specified key, if the key is present
# inserts the key with specified value if does not exists in dictionary
print(".setdefault()\n")
detail.setdefault("Company","Freelancer")
print(detail)

print("="*50)
print()

# dict.popitem() removes the last inserted key-value pair
print("dict.popitem()\n")
detail.popitem()
print(detail)

print("="*50)
print()

# dict.pop() removes the element with specified key
print("dict.pop()\n")
detail.pop("Surname")
print(detail)

print("="*50)
print()

# dict.items() returns list containing tuple for each key value pair
print("dict_items()\n")
a = detail.items()
print(a)

print("="*50)
print()

# dict.fromkeys(sequence, default_value) returns a dictionary with the
# specified keys and specified value
print("dict.fromkeys(sequence, default_value)\n")
tup = ("Name", "Surname", "Age", "Company", "Location")
values = "Default"
detail = detail.fromkeys(tup,values)
print(detail)

print("="*50)
print()

# dict_copy() returns a copy of the dictionary
print("dict_copy()\n")
duplicate = detail.copy()
print("Identity of detail: ",id(detail))
print(detail)

print()

print("Identity of duplicate: ", id(duplicate))

print("="*50)
print()

# dict.get(key, message) returns the value for the given key
print("dict.get(key, message)\n")
a = detail.get("Name","No such key present")
print(a)

print("="*50)
print()

# finding length of the dictionary
print("Length of dictionary: ",len(detail))
print(detail)

print("="*50)
print()

# dict.clear() this will remove all the elements from the dictionary
detail.clear()
print(detail)

print("="*50)
print()
