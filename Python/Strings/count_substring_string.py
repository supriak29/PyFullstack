# counting sub string we use count() method

# main_string.count(substring)
# main_string.count(substring, begin, end)

main_string = input("Enter main string: ")
sub_string = input("Enter sub string to be searched: ")

num = main_string.count(sub_string, 328, -290)
print(num)

# count() method using starting and ending indexing numbers

main_string = input("Enter main string: ")
sub_string = input("Enter substring: ")

## print(len(main_string))

num = main_string.count(sub_string, 0, 74)
print(num)
