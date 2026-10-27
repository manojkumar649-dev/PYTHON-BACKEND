'''
from itertools import permutations

numbers = [1, 2, 3, 4]

result = list(permutations(numbers))

print("All permutations:")
for i in result:
    print(i)

print("Total permutations:", len(result))


TASK 2

from itertools import combinations

values = ['animal', 'birds', 'humans', 'flowers', 'plants']

result = combinations(values, 2)

for i in result:
    print(i)
'''

TASK 4

name = 'programming'

frequency = {}

for i in name:
    print(i)

    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Character frequency:")

for key, value in frequency.items():
    print(key, ":", value)
