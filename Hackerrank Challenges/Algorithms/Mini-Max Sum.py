def miniMaxSum(arr):
    arr.sort()
    min_sum = 0
    max_sum = 0

    for i in range(len(arr) - 1):
        min_sum += arr[i]

    i = 1
    while i != len(arr):
        max_sum += arr[i]
        i += 1

    print(str(min_sum) + " " + str(max_sum))
    print("max sum: %d" % max_sum)
    print("min sum: %d" % min_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
