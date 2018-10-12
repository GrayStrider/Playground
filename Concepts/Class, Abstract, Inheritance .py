"""

Title: $title
Author: $author
Price: $price

REV - Class, Absctract, inheritance

"""

from abc import ABCMeta, abstractmethod


# A Class is like an object constructor, or a "blueprint" for creating objects.
class Book(metaclass=ABCMeta):
    def __init__(self, title, author):
        # Default values can be set here. Values without default can't be skipped during initialisation.
        # __init__ function is called every time new object of a class is created.
        self.title = title
        self.author = author
        self.type = "Book"

    @abstractmethod
    def display(self): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)  # initialising the superclass. "Book" can be replaced by "super()".
        self.price = price

    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))


title = "LOTR"  # input()
author = "Tolkien"
price = 100
new_novel = MyBook(title, author, price)
new_novel.display()
novel2 = Book(title, author)
print(novel2.author)
