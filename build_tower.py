#!/usr/bin/env python2

"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""


def tower_builder(n_floors):
    tower_list = []

    for cur_floor in range(1, n_floors + 1):
        cur_floor_elements = 2*cur_floor - 1
        blank_space = ' ' * (n_floors - cur_floor)
        tower_list.append(blank_space + '*' * cur_floor_elements + blank_space)
    return tower_list

# -------------- clever solutions ---------------------
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
