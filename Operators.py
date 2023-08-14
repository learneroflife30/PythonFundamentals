# Ar-thematic operators

print(5 + 2)  # plus
print(5 - 2)  # minus
print(5 * 2)  # multiply
print(5 / 2)  # divide
print(5 // 2)  # it will remove the part after decimal.
print(5 % 2)  # modula or remainder operator. It will provide the remainder left.
print(5 ** 2)  # it means 5 to the power of 2
print(3 ** 3)  # it means 3 to the power of 3

i = 5
i = i + 2
i += 2  # alternate way of writing as above.
i -= 2
i *= 2

# Operator precedence, using BODMAS rule

result = 2 + 3 * 3
print(result)

# Comparison operators

print(3 > 1)  # greater than
print(3 < 1)  # less than
print(3 >= 1)  # greater than equal to
print(3 <= 1)  # less than equal to
print(3 == 3)  # equal to
print(3 != 3)  # not equal to
print(3 != 1)  # not equal to

# logical operators

print(3 > 2 or 10 < 2)  # OR operator. When either of the conditions is true.
print(30 > 10 and 20 < 9)  # AND operator. When both of the condition needs to be true.
print(not 25 > 30)  # NOT operator. It reverses the expected normal outcome.
