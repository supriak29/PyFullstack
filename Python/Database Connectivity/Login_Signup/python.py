import bcrypt

password = b"abc123"
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
hashed
pwd = bcrypt.checkpw(password,hashed)


if bcrypt.checkpw(password,hashed):
    print("Password Matched!")
else:
    print("Wrong Password!")
