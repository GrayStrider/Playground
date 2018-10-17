"""

REV-- - private elements via __.

Find the largest difference between the elements in the array.

"""


class Difference:
    def __init__(self, a):
        self.__elem = a
        self.maximumDifference = None

    def computeDifference(self):
        self.__elem.sort()
        self.maximumDifference = self.__elem[len(self.__elem) - 1] - self.__elem[0]


a = [1, 5, 6, 8, 10]
