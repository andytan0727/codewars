#!/usr/bin/env python2

"""
Build Tower Advanced

Build Tower by the following given arguments:
number of floors (integer and always greater than 0)
block size (width, height) (integer pair and always greater than (0, 0))

Tower block unit is represented as *

Python: return a list;
JavaScript: returns an Array;
Have fun!

for example, a tower of 3 floors with block size = (2, 3) looks like below

[
  ['    **    '],
  ['    **    '],
  ['    **    '],
  ['  ******  '],
  ['  ******  '],
  ['  ******  '],
  ['**********'],
  ['**********'],
  ['**********']
]
and a tower of 6 floors with block size = (2, 1) looks like below

[
  '          **          ', 
  '        ******        ', 
  '      **********      ', 
  '    **************    ', 
  '  ******************  ', 
  '**********************'
]
Go take a look at Build Tower which is a more basic version :)
"""

def tower_builder(n_floors, block_size):
    w, h = block_size
    ground_floor_elements = w*(1 + 2*(n_floors - 1))
    tower_list = []
    for floor in range(n_floors):
        cur_floor_elements = w*(1 + 2*floor)
        count = 0
        while count < h:
            tower_list.append(('*'*cur_floor_elements).center(ground_floor_elements))
            count += 1
    return tower_list

# ------------------ clever solutions ------------------------------
# def tower_builder(n, (w, h)):
#     return [str.center("*" * (i*2-1)*w, (n*2-1)*w) for i in range(1, n+1) for _ in range(h)]

# def tower_builder(n_floors, block_size):
#     w, h = block_size
#     return [('*' * (w  * (i // h * 2 + 1))).center(w  * ((n_floors - 1) * 2 + 1)) for i in range(n_floors * h)]