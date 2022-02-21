# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:48:54 2021

@author: jsg
"""

import numpy as np
"""
Generate and print a random, legal, 
starting position for chess 960.
"""


def replace_char(s, char="", index=0):
    # Replace character at index in str s with char, return s
    return s[:index] + char + s[index + 1:]


king = "K"
queen = "D"
rook = "T"
bishop = "L"
knight = "S"
hilsen = "Lykke til!"

lisemin = "<3"
s = "abcdefgh"
verbose = False

if verbose:
    print(" ", s)

n = np.random.randint(4)  # Light-squared bishop
s = replace_char(s, bishop, (2 * n) + 1)
if verbose:
    print(n, s)

n = np.random.randint(4)  # Dark-squared bishop
s = replace_char(s, bishop, (2 * n))
if verbose:
    print(n, s)

n = np.random.randint(6)  # Queen
# Getting the still available positions
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, queen, pos[n])
if verbose:
    print(n, s)

 
n = np.random.randint(5)  # First Knight
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, knight, pos[n])
if verbose:
    print(n, s)

n = np.random.randint(4)  # Second  Knight
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, knight, pos[n])
if verbose:
    print(n, s)

# Rook, King and Rook
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, rook, pos[0])
s = replace_char(s, king, pos[1])
s = replace_char(s, rook, pos[2])
print(" ", s, " ", hilsen)
