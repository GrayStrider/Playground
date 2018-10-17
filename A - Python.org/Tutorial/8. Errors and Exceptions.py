"""

https://docs.python.org/3/tutorial/errors.html

"""


# 8.1. Syntax Errors --------------------------------------- #

# 8.2. Exceptions --------------------------------------- #

# TODO 8.3. Handling Exceptions --------------------------------------- #
# 1 --------------------------------------- #
def Convert(s):
    try:
        return int(s)
    except ValueError:
        return "Bad String"


S = input("Enter an int: ").strip()
print(Convert(S))

# 2 --------------------------------------- #
while True:
    try:
        x = int(input("Please enter a number: "))
        print(x)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Class, subclassing --------------------------------------- #
"""
A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class). For example, the following code will print B, C, D in that order:
"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# 8.4. Raising Exceptions --------------------------------------- #
class RandomError(Exception):
    def __init__(self, comment=None):
        print("Very terrible thing happened. Comment: %s" % comment)
        # raise is interrupted and thus overriden by another:
        raise NameError("This is an instance of built-in exception class.")


def error(n):
    if n == 1:
        raise RandomError('HiThere')
    elif n == 2:
        raise RandomError('Error code: 2')


error(2)

"""
If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:
"""


def error2():
    try:
        raise NameError('HiThere')
        # exception is raised...
    except NameError:
        # but intercepted by except first.
        print('An exception flew by!')
        # and then you can raise it again!
        raise


error2()
