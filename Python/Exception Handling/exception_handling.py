### an exception handling example
##
##try:
##    print("This is try block")
##except:
##    print("This the except block") #handler
##else:
##    print("This is an else block")
##finally:
##    print("This is finally block")

############################################
##
##The following points for exception handling
##
##1. A single try block can be followed by several except blocks
##2. Multiple except blocks can be used to handle multiple exceptions
##3. We cannot write except blocks without a try block
##4. We can write a try block without any except blocks
##5. Else block & finally blocks are not compulsory
##6. When there is no exception, else block is executed after try block
##7. Finally block is always executed.

################################################

try:
    f = open("myfile.txt","w")
    a,b = [int(x) for x in input("Enter two numbers: ").split()]
#   a.append(b)
    c = a/b
#   f.write(f'Writing(c) into myfile')

## except blocks are also called handlers
except ZeroDivisionError:
    print("Division by Zero happened")
    print("Please do not enter 0 in denominator")

except AttributeError:
    print("Attribute Not Supported. Attributed Error")

#except ValueError:
#   print("Please enter values seperated by space")

#except IOError:
#   print("User stopped the program")

#except KeyboardInterrupt:
#   print("User stopped the program")

#finally block will always
finally:
    f.close()
    print("File is closed")
