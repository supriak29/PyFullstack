import random as r

# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ",otp)
    return otp

a = otpgen()
c = 1
for c in range(1,4):
    b = input("\nEnter Verification code: ")

    if b == a:
        print("\ncode is correct")
        print("\nSuccessfully Registered.\n")
        break
    else:
        print("Wrong code. Try Again")
        c += 1
        continue
if c > 3:
    print("3 attempts over! Code expired!")
