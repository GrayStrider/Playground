"""

3
sam 99912222
tom 11122222
harry 12299933
sam
tom
jerry

Reading space-separated input
stripping \n character from stdin

"""

# REV - aliases
import sys as s

book = {}
# fill the dictionary
for i in range(int(input())):
    name, number = input().split()
    book[name] = number

# compare with dictionary and print the results
for line in s.stdin:
    line_ = line.rstrip("\n")
    if line_ in book:
        print("%s=%s" % (line_, book[line_]))
    else:
        print("Not found")
