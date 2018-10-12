"""

Heraldo Memelli 8135627 (First, Last, id)
2 (number of scores)
100 80 (scores)

Really bad. Too long, to grindy. Too bad.

"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.s = scores

    def calculate(self):
        if int(sum(self.s) / len(scores)) in range(90, 101):
            return "O"
        elif int(sum(self.s) / len(scores)) in range(80, 91):
            return "E"
        elif int(sum(self.s) / len(scores)) in range(70, 81):
            return "A"
        elif int(sum(self.s) / len(scores)) in range(55, 71):
            return "P"
        elif int(sum(self.s) / len(scores)) in range(40, 56):
            return "D"
        elif int(sum(self.s) / len(scores)) < 40:
            return "T"
        else:
            return 0


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
