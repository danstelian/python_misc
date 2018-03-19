from itertools import groupby
from collections import defaultdict
from operator import itemgetter


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# to use groupby, the list must be firs sorted by the desired field
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(f'\t{i}')


print('-'*100)


# same thing with defaultdict
by_date = defaultdict(list)

# rows don't have to be sorted
f = itemgetter('date')
for row in rows:
    by_date[f(row)].append(row)

for key in sorted(by_date.keys()):
    print(f'{key}')
    for item in by_date[key]:
        print(f'\t{item}')