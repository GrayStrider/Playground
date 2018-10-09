"""

Calculates the decimal ratio of positives, negatives and zeroes
in the array.

"""


def calculateRatio(arr):
    num_positive = num_negative = num_zeroes = 0
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

    # example of "g" string type, removes insignificant trailing zeroes.
    print("Ratio of positives: %g" % rat_positive)
    print("Ratio of negatives: %g" % rat_negative)
    print("Ratio of zeroes: %g" % rat_zeroes)


arr = [1, 1, 0, -1, -1]
calculateRatio(arr)
