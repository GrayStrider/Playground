"""

Find the difference between the
sums of diagonales of
square matrix.

"""

arr1 = [5, 2, 2, 4]
arr2 = [3, 4, 5, 4]
arr3 = [30, 2, 20, 5]
arr5 = [30, 2, 20, 5]

arr4 = [arr1, arr2, arr3, arr5]


def arr_diagonal_difference(arr):
    j = left_sum = right_sum = sum = 0
    for i in range(len(arr)):
        left_sum += arr[i][j]
        j += 1
    print("left sum = %d" % left_sum)
    j = len(arr) - 1
    for i in range(len(arr)):
        right_sum += arr[i][j]
        j -= 1
    print("right sum = %d" % right_sum)
    sum = abs(left_sum - right_sum)
    return sum


print(arr_diagonal_difference(arr4))
