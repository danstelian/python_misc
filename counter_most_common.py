"""
Experimenting with Python's Counter data type!

Counter is a container that keeps track of how
many times equivalent values are added.

Just like a dictionary (it's a dict subclass),
except values can be positive/negative integers.

It's an unordered collection where elements are
stored as keys.
"""


from collections import Counter


# initialization - from list
names = ['Anna', 'Dan', 'John', 'Dave', 'Dan', 'Jimmy', 'Ash', 'Anna', 'Dan', 'Nicolas']
count_names = Counter(names)

# count_names.most_common(3) it's a list of tuples
for item, count in count_names.most_common(3):
    print(f'{item}: {count}')


# initialization - from dict
food = dict(spam=3, toast=2, ham=0, eggs=5)
count_food = Counter(food)

for item, count in count_food.most_common(5):
    print(f'{item}: {count}')


# most regular dict methods are available
print(count_names.keys())
print(count_food.values())
print(count_food.items())


# and back to list
food_list = list(count_food.elements())
# not in the same order
print(food_list)


# indexing
eggs = count_food['eggs']
# returns 0 if element not found
# case in which a dict raises an error
bread = count_food['bread']
print(bread)


# add counts
count_food['spam'] += 1
# new entry
count_food['bread'] = 99

# update will increment the value
count_food.update({'bread': 1})  # a dict
count_food.update(['bread'])  # a list, one of each
print(count_food['bread'])  # bread = 101


# subtract
count_food['bread'] -= 100
print(count_food['bread'])  # bread = 1

# remove altogether
del(count_food['spam'])
print(count_food)  # no spam in the Counter
print(count_food['spam'])  # no error!!! returns 0 :)


# subtracting counts
money = dict(Bitcoin=3, Ethereum=15, Ripple=347, Stellar=2348)
shield = {'Ethereum': 3, 'Stellar': 257}
sword = {'Bitcoin': 1, 'Ripple': 89}
gloves = ['Ethereum']  # one

wallet = Counter(money)

# buy a shield
wallet.subtract(shield)

# buy a sword
wallet.subtract(sword)

# buy gloves
wallet.subtract(gloves)  # minus one Ethereum

# buy freedom
freedom = dict(Bitcoin=99, Ethereum=199, Ripple=1999, Stellar=9999)
wallet.subtract(freedom)

print(wallet)  # damn!


# game over
wallet.clear()
