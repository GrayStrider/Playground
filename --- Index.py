"""

TODO
FIXME
REV - stuff to review.

"""


# REV  - Class
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
    # Default values can be set here. Values without default can't be skipped during initialisation.
    # __init__ function is called every time new object of a class is created.
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.species = "Homo Sapiens"
        
        
# REV - s instead of self


# REV - multiline input, sort of. Not the best example I think
a = []
while input() != "\n":
    a.append(input())
print(a)


# REV - "range" inclusiveness
# starts from 1, ends at 4.
for i in range(1,5):
    print(i)
