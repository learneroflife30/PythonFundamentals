name = "Tony Stark "

print(name)
print(name.upper())  # to convert characters to uppercase
print(name.lower())  # to convert characters to lowercase

print(name.index('r'))  # to find position of character
print(name.index('S'))  # incase index is not present then we get -1 in output

ReplacedName = name.replace('Tony' ,'Mony')  # to replace value of string
print(ReplacedName)

check = "Stark" in  name # to check if character is present or no in string
checkagain = 'D' in name
print(check)
print(checkagain)