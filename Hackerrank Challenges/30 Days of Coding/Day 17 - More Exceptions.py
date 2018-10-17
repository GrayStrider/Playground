"""

In:
4
3 5
2 4
-1 -2
-1 3

Out:
243
16
n and p should be non-negative
n and p should be non-negative


The excercise is little bit different in implementation, but w/e
"""


class ErrorNegative(Exception):
    def __init__(self):
        print("n and p should be non-negative")


class Calculator:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def power(self):
        if self.__x < 0 or self.__y < 0:
            raise ErrorNegative
        else:
            return self.__x**self.__y


A = Calculator(2,-7)
print(A.power())
