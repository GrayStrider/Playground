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
