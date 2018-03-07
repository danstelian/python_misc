"""
Return a new instance of the named tuple
replacing specified fields with new values
"""
from collections import namedtuple


# Weather = namedtuple('Weather', 'city temp_lo temp_hi prcp date')
# alternative way of named tuple initialization
Weather = namedtuple('Weather', ['city', 'temp_lo', 'temp_hi', 'prcp', 'date'])

cw1 = Weather('Brasov', 2, 7, 0.0, '07.03.2018')

city2 = {'city': 'Bucuresti', 'temp_lo': 5, 'temp_hi': 13, 'prcp': 0.25, 'date': '07.03.2018'}
cw2 = Weather(**city2)  # convert a dictionary to a named tuple

print(cw1.prcp)
# cw1 = ... !!!
cw1 = cw1._replace(prcp=0.5) # it's beginning to rain
print(cw1.prcp)
