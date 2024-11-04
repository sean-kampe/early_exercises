#1
# the value of counter is never updated

#2
# age = int(input('How old are you?\n'))
# print(f'You are {age} years old')
# for num in range(1,5):
#     val = num * 10
#     new_age = val + age
#     print(f"In {val} years you will be {new_age}")

#3
my_list = [6, 3, 0, 11, 20, 4, 17]
counter = 0
while counter < len(my_list):
    print(my_list[counter])
    counter += 1

for num in my_list:
    print(num)

#4
count = 0
while count < len(my_list):
    num = my_list[count]
    if num % 2 == 0:
        print(num)
    count += 1
for num in my_list:
    if num % 2 != 0:
        print(num)

#5
my_list2 = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
for value in my_list2:
    for digit in value:
        if digit % 2 == 0:
            print(digit)

#6
my_list3 = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
new = list()
for n in my_list3:
    if n % 2 == 0:
        new.append('even')
    else:
        new.append('odd')
print(new)

#7
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
def find_integers(tup):
    ints = [item for item in tup if type(item) is int]
    return ints

integers = find_integers(my_tuple)
print(integers)

#8
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

dictionary = {ele:len(ele) for ele in my_set if len(ele) % 2 != 0}
print(dictionary)

#9
def factorial(num):
    total = 1
    counter = 1
    while counter <= num:
        if counter == num:
            total *= num
            counter += 1
        else:
            total *= counter * (counter + 1)
            counter += 2
    return total

#10
# import random
#
# highest = 10
#
# def num(n):
#     return random.randrange(n + 1)
#
# temp = num(highest)
# print(temp)
#
# while temp != highest:
#     print(temp)
#     temp = num(highest)
#     if temp == highest:
#         print(temp)

#11
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
counter = 0
temp = 0
while temp < len(my_list):
    while counter < len(my_list[temp]):
        num = my_list[temp][counter]
        if num % 2 == 0:
            print(num)
        counter += 1
    temp += 1
    counter = 0