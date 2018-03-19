from itertools import compress
from random import randint


# filter vs list comprehensions (eg 1)
nums = [randint(-9, 10) for i in range(15)]

positive = [num for num in nums if num > 0]
negative = list(filter(lambda num: num < 0, nums))

print(f'positive: {positive}\nnegative: {negative}', end='\n\n')


# filter vs list comprehensions (eg 2)
def is_int(val):
    try:
        num = int(val)
        return True
    except ValueError:
        return False


values = ['1', '0', '2', '-3', '-', '4', 'N/A', '5']

numbers = list(filter(lambda val: is_int(val), values))
# or
numbers = list(filter(is_int, values))
# finally
numbers = list(map(int, filter(is_int, values)))
print(numbers)

# with list comprehension - a more refined result
# a list comprehension (or generator expression) has the power to transform the data at the same time
numbers = [int(num) if int(num) > 0 else abs(int(num)) for num in values if is_int(num) and int(num) != 0]
print(numbers, end='\n\n')


# compress vs list comprehensions
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]

zips = [5, 5, 5, 2, 5, 1, 4, 1]

zip5 = [n == 5 for n in zips]

new_addresses = list(compress(addresses, zip5))
# print(*new_addresses, sep=', ')

# list comprehension
new_addresses = [addr for index, addr in enumerate(addresses) if zip5[index]]
print(*new_addresses, sep=', ')