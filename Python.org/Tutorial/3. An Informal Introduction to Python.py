"""

Comments, docstrings #
    //, power - ** and ^

Concatenate string, multiply
String subscriptions, as in array. print("word"[3]) = d.
Negative indicing: counting from the right: string[-1] = g

result of an empty  string slice isn't None! Intuitevely, it's "" - an empty string. If we apply that to an array, the result will be the empty array.
slicing: word[0:1] = w, word[0:0] = "".
slice through whole list - [0:-1].
a = [1,2]
You can use out-of-range indexes for slicing, it would just use the edge of the list as a point.
INBETWEEN:
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

Python strings are immutable. Create new one instead: "word" + w.
len("123") = 3

"""


def test():
    """This is a docstring."""
    pass


# This is separator. --------------------------------------- #

class this:
    pass


print(9 // 4)
print(2 ^ 4, 2 ** 4)

print("C:\\test\\directory\\")

# REV- Multiline print
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print("what does this line of long code do"
      "that")

w = "word"
if w[0:-1] is "":
    print(w)
else:
    print(w)

print("word" + w)


# SNIPPETS --------------------------------------- #
# I might add this to to-do formatting, sort of Index. You can see the entries on the right, good enough.
# "comm" expands to the line up there. Take a look at $END$, it places the cursor after the expansion is complate.
# For some reason it expands indented after any indented code,
# even when the snippet itself is being typed on the new unindented line.

# define: --------------------------------------- #
def test():
    pass


# Shallow and deep copy --------------------------------------- #

list = [1, 2, 3]
print(list)
list2 = list
print(list2)
list3 = list[:]
list[1] = 10
print(list)
print(list3)


# for deep copy use "copy" built-in library, deepCopy function.
# Or: a = [1,2,3] a_copy = a[:]


class test2:
    pass


# Test --------------------------------------- #
def test2():
    pass

# Multiple assignment: a,b = 2,3
# order of operations:
# -3**2 = -9, as for -(3**2).
