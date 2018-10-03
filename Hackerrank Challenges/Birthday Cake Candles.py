"""

1c for each year of her total age
only the tallest ones
print the total amount

https://www.hackerrank.com/challenges/birthday-cake-candles/problem

"""


def birthdayCakeCandles(arr):

    # if array is 1
    if len(arr) == 1:
        return 1

    # you can probably sort it backwards and remove the "candles". Eh, meh. TODO
    arr.sort()

    # if all array elements are equal
    if arr[len(arr) - 1] == arr[0]:
        return len(arr)

    max = arr[len(arr) - 1]
    candles = 0
    i = 1

    # compare all from the last with the max, increment
    while arr[len(arr) - i] == max:
        candles += 1
        i += 1

        # prevent OOB
        if i == len(arr):
            break

    return candles


arr = [3, 2, 1, 3]
print(birthdayCakeCandles(arr))
