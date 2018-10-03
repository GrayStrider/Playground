arr = [1, 1, 0, -1, -1]


def calculateRatio(arr):
    num_positive = num_negative = num_zeroes = 0
    rat_positive = rat_negative = rat_zeroes = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            num_negative += 1
        elif arr[i] > 0:
            num_positive += 1
        else:
            num_zeroes += 1

    rat_positive = num_positive / len(arr)
    rat_negative = num_negative / len(arr)
    rat_zeroes = num_zeroes / len(arr)

    rat = [rat_positive, rat_negative, rat_zeroes]
    print(rat_positive)
    print(rat_negative)
    print(rat_zeroes)

    return rat


calculateRatio(arr)
