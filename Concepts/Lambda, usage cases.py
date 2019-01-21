"""

Lambda is small anonimous function.
Lambda can have multiple arguments, but only one expression.

"""


# Creates a function that multiplies a number on "n".
def create_multi(n):
    def __multi(a):
        return a * n

    return __multi


doubler2 = create_multi(2)


# Same, but using lambda function. I can omit "__multi", I don't ever need to call it directly.
def create_multi_lambda(n): return lambda a: a * n


doubler = create_multi_lambda(2)
print(doubler(3))  # 6
