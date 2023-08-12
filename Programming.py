# Python is a case Sensitive language
# to print anything

print('Hello World!')

# Variables in Python
# Variables define memory location where data is stored

name = 'Divyanshu'
age = 22

print(name)
print(age)

# We can change values of variables

name = 'Divyanshu Sharma'
age = 30

print('new name is ' + name)
print('new age is ' + age)

# types of variable

# integer type
age = 29

# floating number
age = 29.0

# boolean, true or false

# in Python, we don't have to declare return type of variable

# excercise

First_Name = 'Tony'
Last_Name = 'Stark'
Age = 51

# for boolean Value
is_genius = True

# input Function helps to take a value and print as a result

name = input("What is your name? ")

# Using concatenation will print the input value i gave
print('Hi ' + name)

# exercise

Super_Hero_Name = input("Hi Tony, please tell your superhero name")
print('Hi, my superhero name is ' + Super_Hero_Name)

# Type conversion
# it is needed as no matter what type of value we give to variable, we get output in string format on print

# int()
# float ()
# str ()
# bool ()

Present_Age = input("Hi whats your age now ? ")

print(Present_Age)

Future_Age = int(Present_Age) + 3  # for integer value

print(Future_Age)


# Code to print sum of two numbers

FirstNumber = input('First number is:')
SecondNumber = input('Second number is:')

total = int(FirstNumber) + int(SecondNumber)

print(total)

