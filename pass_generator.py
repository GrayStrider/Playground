from random import randint as rnd
from string import ascii_letters as letters

letters = list(letters) + [str(i) for i in range(11)] + ['_' for i in range(3)]

# print whole list
print(''.join([letters[i] for i in range(len(letters))]))
# print 25 random symbols from letters (notice len-1)
print(''.join([letters[rnd(0, len(letters) - 1)] for i in range(25)]))
