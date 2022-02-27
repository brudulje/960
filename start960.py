# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:48:54 2021

@author: jsg
"""

import numpy as np
import argparse
# import csv
import json
"""
Generate and print a random, legal, 
starting position for chess 960.
"""
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Increase output verbosity",
                    action="store_true")
parser.add_argument("-l", "--language", type=str,
                    default="no", help="Choose language",)
args = parser.parse_args()

# Read languages from file:
with open("languages.json", "r") as infile:
    lang = json.load(infile)

# Set language
if args.language in lang.keys():
    language = lang[args.language]
else:
    # If language does not exist, set default and report missing language.
    language = lang[parser.get_default('language')]
    print(f"Language '{args.language}' not found, defaulting to Norwegian.")
    print("Valid languages are: ", end="")
    print([k for k in lang.keys()])

king = language[0]
queen = language[1]
rook = language[2]
bishop = language[3]
knight = language[4]
hilsen = language[5]


def replace_char(s, char="", index=0):
    # Replace character at index in str s with char, return s
    return s[:index] + char + s[index + 1:]


s = "abcdefgh"
if args.verbose:
    print(" ", s)

n = np.random.randint(4)  # Light-squared bishop
s = replace_char(s, bishop, (2 * n) + 1)
if args.verbose:
    print(n, s)

n = np.random.randint(4)  # Dark-squared bishop
s = replace_char(s, bishop, (2 * n))
if args.verbose:
    print(n, s)

n = np.random.randint(6)  # Queen
# Getting the still available positions
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, queen, pos[n])
if args.verbose:
    print(n, s)
 
n = np.random.randint(5)  # First Knight
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, knight, pos[n])
if args.verbose:
    print(n, s)

n = np.random.randint(4)  # Second  Knight
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, knight, pos[n])
if args.verbose:
    print(n, s)

# Rook, King and Rook
pos = [i for i, n in enumerate(s) if n in 'abcdefgh']
s = replace_char(s, rook, pos[0])
s = replace_char(s, king, pos[1])
s = replace_char(s, rook, pos[2])
print(" ", s, " ", hilsen)
