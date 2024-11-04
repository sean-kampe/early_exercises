#1. def set_foo():
#     foo = 'bar'
#
# set_foo()
# print(foo)

# Error, foo is only available in the local function scope

# 2. foo = 'bar'
#
# def set_foo():
#     foo = 'qux'
#
# set_foo()
# print(foo)

# prints bar, qux is assigned in the function but in global scope bar is
# still assigned to foo

# 3.
def multiply(num_1, num_2):
    return num_1 * num_2

first = int(input('Enter your first number:\n'))
second = int(input('Enter your second number:\n'))
result = str(multiply(first, second))
print(str(first) + '*' + str(second) + '=' + result)


# 4. def multiply_numbers(num1, num2, num3):
#     result = num1 * num2 * num3
#     return result
#
# product = multiply_numbers(2, 3, 4)

# Name multiply_numbers, argument 2,3,4, def = all function lines, body = the
# second 2 lines, parameters = num1, num2,num3, invocation = product =
# multiply_numbers(2, 3, 4), return = 24, identifiers = multiply_numbers,
# num1, num2, num3, result, and product

# 5. nothing

# 6. nothing, the code returns None before it hits the print statement

# 7. Error, one only argument given and required 2

# 8. Error, 3 arguments given and required 2

# 9. prints 42, 3.141592, 2.718

# 10. prints 42, 3.141592, 2