# 7. The code will print hello to Victor 3 times, then reaassign the NAME
# variable to Nina and print hello 3 times to Nina. It overwrites the variable.

# 8 and 9
balance = 1000
for i in range(5):
    balance += balance * .05
print(balance)

# 10.
# obj = 'ABcd' reassign
# obj.upper() neither
# obj = obj.lower() reassign
# print(len(obj)) neither
# obj = list(obj) reassign
# obj.pop() mutate
# obj[2] = 'X' mutate
# obj.sort() mutate
# set(obj) neither
# obj = tuple(obj) reassign