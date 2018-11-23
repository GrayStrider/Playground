"""
TODO Unique set probability
Would be interesting to play around with this, to calculate probability of full set of uniques appear! How many iterations it would take etc.

"""

from random import randint as rnd

a = [rnd(-10, 10) for i in range(20)]
print(a, len(a))
a = set(a)
print('uniques only:')
print(sorted(a), len(a))
