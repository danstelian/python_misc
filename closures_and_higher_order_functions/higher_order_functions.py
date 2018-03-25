# first - a function takes another function as an argument
def my_map(func, alist):
    result = []

    for item in alist:
        result.append(func(item))

    return result


def square(x):
    return x * x


def cube(x):
    return x * x * x


squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])


# second - a function returning another function
def html_tag(tag):

    def wrap_msg(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_msg


h1 = html_tag('h1')
h1('Headline')

p = html_tag('p')
p('Paragraph')
