"""

REV - private elements via __.

"""


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None

    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = self.__elements[len(self.__elements) - 1] - self.__elements[0]
