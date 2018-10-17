"""

Still spending bunch of time on stupid mistakes.
Interfaces, allow implementing Polymorphism. Seems pretty simple, fine for now.

"""


class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    sum = 0

    def divisorSum(self, n):
        for i in range(n):
            if n % (i + 1) != 0:
                # print("Not divisible")
                continue
            # print("i = %d" % (i + 1))
            self.sum += (i+1)
        return self.sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
