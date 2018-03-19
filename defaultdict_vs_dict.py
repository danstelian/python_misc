from collections import defaultdict


food = {
    'breakfast': {'milk', 'cereal', 'banana', 'eggs'},
    'lunch': {'pizza', 'apple'},
    'dinner': {'soup', 'bread', 'wine'}
}

# dictionary first case
try:
    food['brunch'].add('yogurt')
except KeyError as e:
    print(e)

# solution
if 'brunch' not in food:
    food['brunch'] = set()
food['brunch'].add('yogurt')
print(food['brunch'])


# dictionary second case
food.setdefault('snack', set()).add('candy bar')
food.setdefault('snack', set()).add('chips')
print(food['snack'])


# defaultdict alternative
default_food = defaultdict(set)
default_food.update({
    'breakfast': {'milk', 'cereal', 'banana', 'eggs'},
    'lunch': {'pizza', 'apple'},
    'dinner': {'soup', 'bread', 'wine'}
})

default_food['appetizer'].add('bruschetta')  # no error
print(default_food['appetizer'])

# curious case
print(default_food['refreshment'])  # this adds a new key and an empty set as value
# print(default_food)
