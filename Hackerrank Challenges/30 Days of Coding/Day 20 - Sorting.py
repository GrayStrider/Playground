"""

Bubble sort.
Track number of swaps, swap elements out of order. If number of swaps is 0 on a traversal, sorting is finished.


Jesus fucking Crist, did it took me long. Wow. Well, at least I can say I did it myself. I'll have to take a look at it later,
I'm not sure that I need deepcopy everywhere?

"""
#
#
# # n = int(input().strip())
# # a = list(map(int, input().strip().split(' ')))
# import copy
#
# def BubbleSort(a):
#     swaps = 0
#
#     for i in range(len(a) - 1):
#         # print("Iteration ", i)
#         print("a[%d] = %d, a[%d+1] = %d" % (i, a[i], i + 1, a[i + 1]))
#         # print("pass %d" % i)
#         pass_swaps = 0
#         # if a[i+1] < a[i]:
#         #     print("a %d is more a i +1" % i)
#         #     a.insert(i, a.pop(i))
#         # print(a[i], end=" ")
#         if a[i + 1] < a[i]:
#             print(a[i + 1], "needs swapping with", a[i])
#             temp = copy.deepcopy(a[i])
#             a[i] = copy.deepcopy(a[i+1])
#             a[i+1] = copy.deepcopy(temp)
#             pass_swaps += 1
#             print("Swaps: ", pass_swaps)
#             print("new array: ", a)
#         else:
#             if pass_swaps == 0:
#                 break
#             continue
#
#
# a = [10, 9, 4, 4, 11]
# BubbleSort(a)
# print("Sorted: ", a)
#

import copy

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def BubbleSort(a):
    swaps = 0
    for j in range(len(a)-1):
        pass_swaps = 0
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = copy.deepcopy(a[i])
                a[i] = copy.deepcopy(a[i+1])
                a[i+1] = copy.deepcopy(temp)
                pass_swaps += 1
            else:
                continue
        if pass_swaps == 0:
            continue
        else:
            swaps += pass_swaps
    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])


BubbleSort(a)
