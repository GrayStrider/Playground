"""

TODO
FIXME

REV- - NEW stuff to review.
REV--  Next iteration
REV--- I remember this very well.
etc.

"""


# REV- - s instead of self


# REV- - multiline input, sort of. Not the best example I think
a = []
while input() != "\n":
    a.append(input())
print(a)


# REV- - "range" inclusiveness
# starts from 1, ends at 4.
for i in range(1,5):
    print(i)
