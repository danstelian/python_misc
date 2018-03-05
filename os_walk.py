"""
Module documentation
This simple script illustrates how a search
can be performed using the os.walk function
(also an excuse to use the os module)
"""
import os


home = os.environ.get('HOME')  # for unknown user, just for kicks
search_dir = os.path.join(home, 'code/')  # search in this directory
to_search = 'upcracker'  # name of file to be searched

for root, dirs, files in os.walk(search_dir):  # os.walk is coded as a recursive function, with 'yield from' (as of 3.3)
    for file_name in files:
        name, ext = os.path.splitext(file_name)
        if name.startswith(to_search) and ext == '.py':  # every file that starts with
            print(f'{name} in {root}')
