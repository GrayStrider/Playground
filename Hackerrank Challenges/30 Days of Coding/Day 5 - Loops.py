"""

"print" formatting.

"""

if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print("%d x %d = %d" % (n, i, n * i))
