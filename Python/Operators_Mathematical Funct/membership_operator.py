# MEMBERSHIP OPERATOR

########################################

# in operator
print("********* in operator *********")

name = ["Ram", "Shyam", "Ghanshyam", "Baburao"]

print("Print True if name Ram is in the name: ", "Ram" in name)

print("Print True if name Shyam is in the name: ", "Shyam" in name)

print("Print False if name Raju is in the name: ", "Raju" in name)

print()
print()

#search in dictionary using in operator
postal = {"Delhi":110001, "Chennai":600001, "Punjab":123456}

# This will return false, as it only searches for the matching keys and not the values
print("Print True if state Delhi is in postal: ",123456 in postal)

print("Print True if state Chennai is in postal: ","Chennai" in postal)

print("Print False if state Maharashtra is in postal: ","Maharashtra" in postal)

print()
print("====================================")
print()

################################################

# not in operator

print("********** not in operator **********")

name = ["Ram", "Shyam", "Ghanshyam", "Baburao"]

print("Print False if name Ram is not in the name: ", "Ram" not in name)

print("Print False if name Shyam is in the name: ", "Shyam" not in name)

print("Print True if name Raju is in the name: ", "Raju" not in name)

print()
print()

#search in dictionary using not in operator
postal = {"Delhi":110001, "Chennai":600001, "Punjab":123456}

# This will return true, as it only searches for the matching keys and not the values
print("Print True if state Delhi is not in postal: ",123456 not in postal)

print("Print False if state Delhi is not in postal: ","Delhi" not in postal)

print("Print False if state Chennai is not in postal: ","Chennai" not in postal)

print("Print True if state Maharashtra is not in postal: ","Maharashtra" not in postal)

print()
print("====================================")
print()

name = "Supriya Sanjay Karkera"

print("Supriya" in name)
print("supriya" in name)
print("K" in name)
print(" " in name)
print("  " in name)
print('j' in name)

print()
print("====================================")
print()

name = ["Supriya", "Sanjay", "Karkera"]


