"""
Some convoluted examples of defaultdict-Counter collaboration
"""


from collections import Counter, defaultdict


food = [('spam', 1), ('toast', 4), ('ham', 2), ('spam', 6), ('eggs', 3)]

default_food = defaultdict(list)

# first element of the tuple becomes the key
# second element of the tuple is added to a list of values
for key, value in food:
    default_food[key].append(value)

for x in default_food.items():
    print(x)
print()


eat = [('spam', 1), ('toast', 4), ('ham', 2), ('spam', 6), ('eggs', 3)]
drink = [('milk', 1), ('water', 4), ('milk', 2), ('juice', 6), ('wine', 3)]

count_food = defaultdict(Counter)

# complicated stuff
# the keys of the dictionary are entered manually 'eat' and 'drink'
# every key stores a Counter object that counts how many times a certain
# element appears in the input list
for key, value in eat:
    count_food['eat'][key] += value
for key, value in drink:
    count_food['drink'][key] += value

print('Best food:')
for x in count_food['eat'].most_common(2):
    print(x)
print('Best drink:')
for x in count_food['drink'].most_common(2):
    print(x)
