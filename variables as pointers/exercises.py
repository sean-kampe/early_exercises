#1
# my_object1 == my_object2
# my_object1 is my_object2
# the first is an expression returning a bool if the 2 objects are equal,
# the second if the 2 objects refer to the same object

#2
# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# since set1 and set2 reference the same object, adding the range object to
# set1 impacts set2 as well since they point to the same object

#3
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# dict2 is a shallow copy and references a different object so mutating a
# key:value pair to dict2 will not impact dict1, thus "The life of brian"
# will print

#4
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# dict1 and dict2 reference two different objects, but the pointers point to
# the same inner list and reference the same object in memory, thus the print
# statement will print the new value 42

#5
import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

#6
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2) #False
print(dict1['a']    is dict2['a']) # True
print(dict1['a'][0] is dict2['a'][0]) # True
print(dict1['a'][1] is dict2['a'][1]) # True
print(dict1['b']    is dict2['b']) # True
print(dict1['b'][0] is dict2['b'][0]) # True
print(dict1['b'][1] is dict2['b'][1]) # True