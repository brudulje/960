# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:48:54 2021

@author: jsg
"""
import numpy as np
import argparse
import json
"""
Generate and print a random, legal,
starting position for chess 960.
"""
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Increase output verbosity",
                    action="store_true")
parser.add_argument("-l", "--language", help="Choose language",
                    type=str, default="no", )
parser.add_argument("-f", "--fen", help="Print FEN string",
                    action="store_true")
args = parser.parse_args()


def replace_char(s, char="", index=0):
    """Replace character at index in str s with char, return s."""
    return s[:index] + char + s[index + 1:]


def english(s):
    """Translate str s to english for the purpose of writing FEN string."""
    for n in range(len(s)):
        s = replace_char(s, char=lang["en"][languages.index(s[n])], index=n)
    return s


def fen(s="TSLDKLST"):
    """Generate FEN string with english notation from s."""
    return english(s).lower() + "/pppppppp/8/8/8/8/PPPPPPPP/" \
        + english(s).upper() + " w KQkq - 0 1"


default_lang = {'no': ['K', 'D', 'T', 'L', 'S', 'Lykke til!'],
                'en': ['K', 'Q', 'R', 'B', 'N', 'Go for it!'],
                }
# Read languages from file and add to default languages,
# keeping the default if there are conflicts:
with open("languages.json", "r") as infile:
    lang = json.load(infile)
lang.update(default_lang)

# Set language
if args.language in lang.keys():
    languages = lang[args.language]
else:
    # If language does not exist, set default and report missing language.
    languages = lang[parser.get_default('language')]
    print(f"Language '{args.language}' not found, defaulting to Norwegian.")
    print("Valid languages are: ", end="")
    print([k for k in lang.keys()])

king = languages[0]
queen = languages[1]
rook = languages[2]
bishop = languages[3]
knight = languages[4]
hilsen = languages[5]

# Now, set up the actual starting position
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
if args.fen:
    print(fen(s))
