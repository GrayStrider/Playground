"""

REV-- Try, Except; error handling

"""


def Convert(s):
    try:
        return int(s)
    except ValueError:
        return "Bad String"


S = input().strip()
print(Convert(S))
