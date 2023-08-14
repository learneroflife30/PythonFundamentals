# List is a non-primitive data type

# list is a collection of items. It is a complex data type. It can have value of multiple types in it like string
# integer etc

marks = [95, 98, 97, "They are marks"]
print(marks)
print(marks[0])
print(marks[2])
print(marks[1])

new_list_of_marks = marks[0:2]
print(new_list_of_marks)

# to add number at end of list
marks.append(100)

# to add number at start of list
marks.insert(0, 99)

# to add number in between list
marks.insert(1, 90)

# print new list
print(marks)

# to check if a number is present or not in list
print(98 in marks)
print(200 in marks)

# to get length of list
print(len(marks))

# to print values in list one by one using while loop

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# to empty the list

EmptyList = marks.clear()
print(EmptyList)

# Tuple  - It is a data structure which is  like a list-but it is immutable unlike list. For example
# in list we can append, clear etc. It can't be done in tuple, once values are declared.
# list is defined in square brackets []
# tuple is defined in parentheses-but it's not compulsory () ,

# tuple
marks = (85, 89, 81, 89)
print(marks)

# to count how many items are present in tuple
print(marks.count(89))
print(marks.count(81))
print(marks.count(80))

# to count index of item present in tuple
print(marks.index(89))
print(marks.index(81))

# tuple without parenthesis example below
toppers = 'Abhi', ' Rahul', 'Jannat'
print(toppers)

# Set
# it is declared with curly braces {}
# in Set's only unique values are printed and not repetitive
# set don't have index, hence to get all values we have to apply a loop

schools = {'Stephens', ' Xaviers', 45, 44, 'Patricks', 33, 'Stephens'}
print(schools)

# using normal for loop to get all values
for school in schools:
    print(school)

# using continue statement
for school in schools:
    if school == 44:
        continue
    print(school)

# using break statement
for school in schools:
    if school == 33:
        print("I am breaking the statement after this")
    break

# Dictionary
# it is important data structure where we store information in key value pair.

marks = {"english": 91, "maths": 99, "history": 81, "chemistry": 94, "physics": 98}
print(marks)

# to get a value or add a value or updated a value in dictionary we pass the key

# to get
print(marks["maths"])

# to add
marks["biology"] = 92
print(marks)

# to update
marks['history'] = 83
print(marks)

