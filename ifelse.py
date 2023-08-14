# if , elif , else statements

age = 30

if age < 20 or age > 50:
    print('Age is not thirty')
elif age > 10 and age >= 30:
    print('Age is equal to thirty')
else:
    print(' Age is almost thirty')

# note : in case of if , all conditions are checked but in case of elif second condition is checked only after
# getting first condition as true.


# break and continue statements

students = ['Jay', 'Akshay', 'Divyanshu', 'Harjeet']

for student in students:
    if student == "Divyanshu":
        continue
    print(student)

for student in students:
    if student == 'Akshay':
        break
