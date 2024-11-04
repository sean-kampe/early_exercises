string = 'Aloha, World!'
print(string.lower())

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
print(fruits.index('cherry'))

print(1_987_654_321)

name = "Victor"
profession = "programmer"

text = 'Hello {}. You are a {}.'
f_text = text.format(name, profession)
print(f_text)
print(f'Hello {name}. You are a {profession}.')

from datetime import datetime

current_time = datetime.now()
print(f'the time is {current_time}')

from datetime import date

today = date.today()

today_year = today.year
print(today_year)
iso_year = today.isocalendar()[0]

import random
random_number = random.randint(0, 1)
print('yes' if random_number == 1 else 'no')

weather = 'cloudy'

match weather:
    case 'rainy':
        print('it is rainy')
    case 'sunny':
        print('it is sunny')
    case _:
        print('lets watch tv')

#--------------------------------------------------------
def is_empty(string):
    return not string # or return string == ''
is_empty(' fs')

def is_empty_or_blank(s):
    if len(s) == 0:
        return not s
    return s.isspace()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

#better
# def is_empty_or_blank(s):
#     return s.strip(' ') == ''

#best
# def is_empty_or_blank(s):
#     return not s.strip(' ')

t = 'launch school tech & talk'

def compare_by_length(a, b):
    val = 0
    if len(a) < len(b):
        val = -1
    elif len(a) > len(b):
        val = 1
    return val
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0



answer = 'Captain Ruby'.split(' ')[0] + ' Python'

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract(s):
    l = s.split('.')[0]
    return l.split('_')[1]
print(extract('engl_KR.UTF-16'))

def local_greet(s):
    if extract_language(s) != 'en':
        return greet(extract_language(s))
    elif extract(s) == 'US':
        return 'Hey'
    elif extract(s) == 'GB':
        return "Hello"
    else:
        return 'Howdy'

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

x = 10

def my_function():
    #x = x + 5
    print(x)

my_function()
# We attempt to reassign the value of x by incrementing it, Python assumes
# that x is a local variable since we're assigning it inside the function.
# However, since it is uninitialized, we get an error.

a = 1

def my_function2():
    print(a)
    #a = 2

my_function2()

# Python detects that a is being assigned within the my_function function and
# therefore treats it as a local variable. However, since we are trying to
# print the local a variable's value before it has been assigned a value,
# we get an error.

b = [1, 2, 3]

def my_function3():
    b[0] = 10

my_function3()
print(b)
# This example shows how lists, being mutable objects, can be modified within
# a function, affecting the original list in the global scope.
# The list b is initialized on line 1 outside the function my_function. Inside
# the function, on line 4, the first element of b is changed to 10. Since b
# is not a local variable within my_function() but we are directly
# referencing b from the global scope, the change b[0] = 10 impacts the
# global variable b. Consequently, after the execution of my_function(),
# the  global list b reflects this modification, and printing b will display
# [10, 2, 3]

def i_empty(s):
    return not s or s.isspace()
print(i_empty('mars'))  # False
print(i_empty('  '))    # False
print(i_empty(''))      # True

b = 'launch school tech & talk'
print(b.title())

def starts_with(a, b):
    return a.startswith(b)
print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

def count_substrings(str, sub):
    return str.count(sub)
print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

def first(l):
    return l[0] if len(l) > 0 else "Empty!"
print(first(['Earth', 'Moon', 'Mars']))  # Earth

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked = grocery_list.pop(0)
    print(checked)
print(grocery_list)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
for item in numbers:
    print(f'the {item} is {numbers[item]}')

for key, value in numbers.items():
    print(f'the new {key} is {value}')


pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'] = ['sparky', 'fido', 'bowser']
# OR BETTER
pets['dog'].append('bowser')

print(pets)


# We can use the list.copy method, which generates a shallow copy of the list
# object. By doing so, the three nested sub-lists will individually reference
# distinct objects. As a result, modifications in one sub-list won't affect
# the others.
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0