
authors = [
    {'name': 'Luciano Ramalho', 'book': 'Fluent Python'},
    {'name': 'David Beazley', 'book': 'Python Cookbook'},
    {'name': 'Mark Lutz', 'book': 'Learning Python'}
]

# say we want to sort by the last name of the author


def criterion(crt):

    def by_lastname(adict):
        name = adict['name']
        return name.split()[-1]

    if crt == 'lastname':
        return by_lastname


for author in sorted(authors, key=criterion('lastname')):
    print(f"{author['name']}: {author['book']}")
