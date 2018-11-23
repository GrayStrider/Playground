from math import sqrt


def fib(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))


def productFib(num: int):
    iteration = 0
    while True:
        result = fib(iteration) * fib(iteration + 1)
        # print(result, fib(iteration), fib(iteration + 1))
        if result >= num:
            if result == num:
                return [fib(iteration), fib(iteration + 1), True]
            else:
                return [fib(iteration + 1), fib(iteration + 2), False]
        iteration += 1


print(productFib(9999999999))

# Please kill me.
