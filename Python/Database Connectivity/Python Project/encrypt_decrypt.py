
import bcrypt
  
# example password
password = input("enter password: ")
  
# converting password to array of bytes
bytes = password.encode('utf-8')
print("bytes: ",bytes)
  
# generating the salt
salt = bcrypt.gensalt()
print("salt: ",salt)

# Hashing the password
hash = bcrypt.hashpw(bytes, salt)
print("hash: ",hash)
  
# Taking user entered password 
userpwd = input("Enter user password: ")
  
# encoding user password
userBytes = userpwd.encode('utf-8')
print("\nuserBytes: ",userBytes)
  
# checking password
result = bcrypt.checkpw(userBytes, hash)
print("result: ",result)
  
print(result)
