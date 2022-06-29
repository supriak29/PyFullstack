# SPLIT and JOIN strings

# main_string.split(pattern)

main_string = "one, two three,four@Five$Six"
split_string = main_string.split('$')
print(split_string)

main_string2 = "one two three four"
split_string2 = main_string2.split()
print(split_string2)


# .split() means splitting based on spaces in the input

list_colors = input("Enter colors with space: ").split()
print(list_colors)

### joining of the string
### seperator.join(string)

joined_string = "-".join(list_colors)
print(joined_string)
