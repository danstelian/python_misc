# Sorting a list of dictionaries by a common key
from operator import itemgetter
from functools import reduce
from collections import OrderedDict


rows = [
    {'first': 'Bob', 'last': 'Smith', 'uid': 1003},
    {'first': 'David', 'last': 'Jones', 'uid': 1002},
    {'first': 'Brian', 'last': 'Heiner', 'uid': 1001},
    {'first': 'Corey', 'last': 'Foster', 'uid': 1005},
    {'first': 'Ben', 'last': 'Smith', 'uid': 1004},
]

# method 1
so_min = sorted(rows, key=lambda t: t['uid'])
# print(so_min)

# method 2
so_max = sorted(rows, key=itemgetter('uid'), reverse=True)
# print(so_max)

# method 3
so_min = sorted(rows, key=lambda t: (t['last'], t['first']))


# method 4
so_max = sorted(rows, key=itemgetter('last', 'first'), reverse=True)


# how to use itemgetter
f = itemgetter('uid')
for row in rows:
    print(f(row), 'is', row['uid'])


# min, max with itemgetter
mi = min(rows, key=itemgetter('uid'))
ma = max(rows, key=itemgetter('uid'))
print(mi, ma, sep='\n', end='\n\n')


# adding (the uid) with reduce
su = reduce(lambda x, y: x + y, [f(row) for row in rows])
# or
su = reduce(lambda x, y: x + y, [row['uid'] for row in rows])
# or the much cleaner version
su = sum([f(row) for row in rows])
print(su, end='\n\n')


# how about OrderedDict objects
ordered = [OrderedDict(row) for row in rows]
for row in sorted(ordered, key=itemgetter('uid')):
    print(row['first'], row['last'])
