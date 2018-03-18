# Sorting objects without native comparison support
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'


users = [User(3), User(23), User(7), User(43)]

# min, max
mi = min(users, key=attrgetter('user_id'))
ma = max(users, key=attrgetter('user_id'))
print(mi, ma, sep='\n')

# sort
so = sorted(users, key=attrgetter('user_id'))
# or
so = sorted(users, key=lambda t: t.user_id)
print(so)


# sum (would make more sence if User had an 'income' attribute or something like that)
g = attrgetter('user_id')
su = sum([g(user) for user in users])
print(su)
