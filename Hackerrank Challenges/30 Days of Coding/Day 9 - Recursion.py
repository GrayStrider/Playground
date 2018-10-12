"""

Factorial.

f(1) = 1.
f(n) = n x f(n-1).
f(2) = (f(1) = 1) x n (2) = 2.
f(3) = f(2) x 3
f(4) = f(3) x 4

....
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


print(factorial(int(input())))
