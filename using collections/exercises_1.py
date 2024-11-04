print(range(0, 25, 3)[6])

string = 'Launch School'
print(string[4:10])

tup_1 = (1, 2, 3, 4, 5)
tup_2 = tuple(reversed(tup_1))
tup_3 = tup_2[1:4]
print(tup_3)

# 4.
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

# 5. Which of the following values can't be used as a key in a dict object,
# and why?----type must be immutable, so not sets, dictionaries or lists,
# all others are okay

#6.
print('abc-def'.isalpha()) #False
print('abc_def'.isalpha()) #False
print('abc def'.isalpha()) #False
print('abc def'.isalpha() and
      'abc def'.isspace()) #False
print('abc def'.isalpha() or
      'abc def'.isspace()) #False
print('abcdef'.isalpha()) #True
print('31415'.isdigit()) #True
print('-31415'.isdigit()) #False
print('31_415'.isdigit()) #False
print('3.1415'.isdigit()) #False
print(''.isspace()) #False

# 7.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = info.replace(':', '+')
print(new_info)

sep = info.split(':')
merge = '+'.join(sep)
print(merge)

#8
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29
# the first line first takes a substring slice and looks for the f in the
# substring, and the second is search in the full string still

#9.
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)

#10
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

#11
# False
# True
# True
# False
# True
# False
# False
# True
# False
# True

#12
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

#13 True, False, True, False

#14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)
combine = zip(my_str, my_list, my_tuple, my_range)
print(list(combine))

#15 Cat, Bird, Snake