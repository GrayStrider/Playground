"""

input:
4
1 4 3 2

output:
2 3 4 1

"""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in reversed(range(len(arr))):
        # print(i)
        print(arr[i], end=" ")
