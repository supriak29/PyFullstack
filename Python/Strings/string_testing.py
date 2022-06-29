# string testing 

# to check if string is alphabet or not
name = input("Enter your name: ")
if name.isalpha():
    print(name)
else:
    print("No")

# to check string is a digit or not
mobile = input("Enter mobile number: ")
if mobile.isdigit():
    print(mobile)
else:
    print("No")

# to check string is a alphabet and numeric or not
captcha = input("Enter captcha")
if captcha.isalnum():
    print(captcha)
else:
    print("No")
