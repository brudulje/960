# 960

## Usage

Create and display a random, legal, starting position for chess960.
The position is written using eight characters representing the chess pieces
starting at the a-file:

Usage:

    $ python 960.py
      SDLLSTKT   Lykke til!

960 has three optional arguments in addition to the `-h` option which will
print the help text to terminal:

    $ python 960.py -h
    usage: 960.py [-h] [-v] [-l LANGUAGE] [-f]

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         Increase output verbosity
      -l LANGUAGE, --language LANGUAGE
                            Choose language
      -f, --fen             Print FEN string

As of v1.0, there are 16 valid languages. Chose your language using the `-l`
option. Spesifying an invalid language
will cause 960 to default to Norwegian and output the list of valid languages:

    $ python 960.py -l x
    Language 'x' not found, defaulting to Norwegian.
    Valid languages are: ['no', 'se', 'dk', 'is', 'fi', 'ee', 'lt', 'lv',
     'pl', 'ir', 'cy', 'nl', 'de', 'en', 'es', 'fr']
      TSLLKDST   Lykke til!

    $ python 960.py -l fr
      CFFTRDTC   Allez!

The `-f` option will give the FEN string for the chosen starting position.
THe FEN string will allways be in English:

    $ python 960.py -l nl -f
      HPDKLLPH   Succes!
    rnqkbbnr/pppppppp/8/8/8/8/PPPPPPPP/RNQKBBNR w KQkq - 0 1

The `-v` option will give a more verbose output, showing the random numbers
which were chosen and how the positions are filled with pieces, using the
lower case letters `abcdefgh` to represent empty squares.

## Behind the scenes

The process of choosing the position is as follows:

Choose a random number 0-3. Place the *light-squared bishop* on the b, d,
f or h file accordingly.

Choose a random number 0-3. Place the *dark-squared bishop* on the a, c,
e or g file accordingly.

Now, there are six empty squares. For the rest of th eprocedure, we count
only empty squares, starting closest to the a-file. Choose a random number
0-5 and place the *queen* accordingly.

Choose a random number 0-4, place a *knight* accordingly.

Choose a random number 0-3, place the other *knight* accordingly.

Now there are three empty squares, and the *king* and both *rooks* are left.
The king should be in the middle and the rooks on the tow last empty squares.

The black and white pieces are symmetricl. If white has a knight on the
a-file, so does black. If white has a rook on the f-file, so does black.

This is the process detailed by the `-v` option.
