import copy


def BubbleSort(a):
    swaps = 0
    for j in range(len(a) - 1):
        pass_swaps = 0
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                temp = copy.deepcopy(a[i])
                a[i] = copy.deepcopy(a[i + 1])
                a[i + 1] = copy.deepcopy(temp)
                pass_swaps += 1
            else:
                continue
        if pass_swaps == 0:
            print("Sorted")
        else:
            swaps += pass_swaps


a = [10, 9, 4, 4, 11, -1, 2, 3]
BubbleSort(a)
print("Sorted: ", a)
