#################
1


# arr = [1,5,6,7,4]
#
# def arr_sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     return sum
#
# print("one-dimensional array")
# print(arr_sum(arr))
#
# arr2 = [3,4,5]
# arr3 = [5,2,2]
# arr = [arr3, arr2]
#
# def arr_sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             sum += arr[i][j]
#     return sum
#
# print("two-dimensional array")
# print(arr_sum(arr))

arr1 = [5,2,2,4]
arr2 = [3,4,5,4]
arr3 = [30,2,20,5]
arr5 = [30,2,20,5]

arr4 = [arr1, arr2, arr3,arr5]

# print(arr4)
# def arr_diagonal_difference(arr):
#     sum = 0
#     left_sum = arr[0][0] + arr[1][1] + arr[2][2]
#     #print("l sum is %d" %left_sum)
#     right_sum = arr[0][2] + arr[1][1] + arr[2][0]
#     #print("r sum is %d" %right_sum)
#     sum = abs(left_sum-right_sum)
#     #print("sum is %d" %sum)
#     return sum

# arr_diagonal_difference(arr4)
# print(arr_diagonal_difference(arr4))

def arr_diagonal_difference(arr):
    j = left_sum = right_sum = sum = 0
    # left_sum = 0
    # right_sum = 0
    # sum = 0
    for i in range(len(arr)):
        left_sum += arr[i][j]
        j += 1
    print("left sum = %d" %left_sum)
    #print(arr4[0][len(arr4)-1]) # last element, arr[0][length-1]
    j = len(arr)-1
    for i in range(len(arr)):
        right_sum += arr[i][j]
        j -= 1
    print("right sum = %d" %right_sum)
    sum = abs(left_sum - right_sum)
    #print("l sum is %d" %left_sum)
    #right_sum = arr[0][2] + arr[1][1] + arr[2][0]
    #print("r sum is %d" %right_sum)
    #sum = abs(left_sum-right_sum)
    #print("sum is %d" %sum)
    return sum
print(arr_diagonal_difference(arr4))
###################
# 2

# arr = [[1, 2, 3], [4,5,6],[7,8,9]]
#
# def matrix_sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         print("\n")
#         for j in range(len(arr)):
#             print(arr[i][j])
#             sum += arr[i][j]
#     return sum
#
# print(matrix_sum(arr))

###################
# 3

# arr_b = [1,2,5,3]
# arr = [[1, 2, 3,4,4], [4,5,6,7],[7,8,9]]
#
# # print(arr[1][3])
#
# def matrix_sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             sum += arr[i][j]
#     return sum
#
# print(matrix_sum(arr))
