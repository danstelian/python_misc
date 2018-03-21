"""
output

a: abcdefghijklmnopqrstuvwxyz
b: bcdefghijklmnopqrstuvwxyza
c: cdefghijklmnopqrstuvwxyzab
d: defghijklmnopqrstuvwxyzabc
e: efghijklmnopqrstuvwxyzabcd
f: fghijklmnopqrstuvwxyzabcde
g: ghijklmnopqrstuvwxyzabcdef
h: hijklmnopqrstuvwxyzabcdefg
i: ijklmnopqrstuvwxyzabcdefgh
j: jklmnopqrstuvwxyzabcdefghi
k: klmnopqrstuvwxyzabcdefghij
l: lmnopqrstuvwxyzabcdefghijk
m: mnopqrstuvwxyzabcdefghijkl
n: nopqrstuvwxyzabcdefghijklm
o: opqrstuvwxyzabcdefghijklmn
p: pqrstuvwxyzabcdefghijklmno
q: qrstuvwxyzabcdefghijklmnop
r: rstuvwxyzabcdefghijklmnopq
s: stuvwxyzabcdefghijklmnopqr
t: tuvwxyzabcdefghijklmnopqrs
u: uvwxyzabcdefghijklmnopqrst
v: vwxyzabcdefghijklmnopqrstu
w: wxyzabcdefghijklmnopqrstuv
x: xyzabcdefghijklmnopqrstuvw
y: yzabcdefghijklmnopqrstuvwx
z: zabcdefghijklmnopqrstuvwxy
"""
from collections import deque
from itertools import cycle, islice
from string import ascii_lowercase


# first method - with deque
catalog = dict().fromkeys(ascii_lowercase, None)
deq = deque(ascii_lowercase)
deq.rotate()

for char in ascii_lowercase:
    deq.rotate(-1)
    catalog[char] = ''.join(deq)

# for k, v in sorted(catalog.items()):
#     print(f'{k}: {v}')


# second method - with islice and cycle
catalog = {k: ''.join([v for v, z in zip(islice(cycle(ascii_lowercase), i, None), ascii_lowercase)]) for i, k in enumerate(ascii_lowercase)}

for k, v in sorted(catalog.items()):
    print(f'{k}: {v}')
