#1.
# False or (True and False) = False
# True or (1 + 2) = True
# (1 + 2) or True = 3
# True and (1 + 2) = 3
# False and (1 + 2) = False
# (1 + 2) and True = True
# (32 * 4) >= 129 = False
# False != (not True) = False
# True == 4 = False
# False == (847 == '847') = True

#2.
def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

#3. first Product2, then Product not found!

#4.
# if foo():
#     return 'bar'
# else:
#     return qux()

#5. It prints Empty because an empty list is falsy, which was passed as an
# argument, so it hits the else block

#6.
def caps(string):
    return (string if len(string) <= 10 else string.upper())

#7.
def number_range(num):
    if num < 0:
        print(f'{num} is less than 0')
    elif num < 51:
        print(f'{num} is between 0 and 50')
    elif num < 101:
        print(f'{num} is between 51 and 100')
    else:
        print(f'{num} is greater than 100')
