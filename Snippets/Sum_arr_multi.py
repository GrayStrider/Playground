"""

Sum of elements in multi-dimentional array.
Looks bad

"""


def sum1(arr):
    sum = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            sum = sum + arr[row][col]
            print(sum)
    return sum


a = [[1, 2], [3, 4], [5, 6]]
sum1(a)

# indexing in the array
b = [1, 2, 3]
for i in b:
    print("value: %d, index: %d" % i, b.index(i))

# "range" class
print(range(2))
print(type(range(2)))

# new line
print("#############\n")
