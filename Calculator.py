# Using an if, elif, else statement in Python , I have built a calculator

first = input("enter the first number: ")
operator = input("enter operator (+,-,*,/,%): ")
second = input("enter second number: ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print('incorrect output')

# note : in case of if , all conditions are checked but in case of elif second condition is checked only after
# getting first condition as true.
