# bytearrays are mutable

name = "This is an example" #bytearray() creation
print(type(name))

bname = bytearray(name,'utf-8')
print(type(bname))
print('The bname is: ',bname)
