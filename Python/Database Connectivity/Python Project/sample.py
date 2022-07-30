from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("key: ",key)
print("Key decode() : ", key.decode())
print()

f = Fernet(key)
print("fernet: ",f)

def encPwd():
    pwd = bytes(input("Enter password: "),'utf-8')
    encrypted_data = f.encrypt(pwd)
    print("After encryption : ", encrypted_data)
    return encrypted_data

def decPwd(encrypted_data):
    decrypted_data = f.decrypt(encrypted_data)
    print(decrypted_data)
    print("After decryption : ", decrypted_data.decode())

encrypted_data = encPwd()
decPwd(encrypted_data)
