""""
A =
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

B =
a b c
  d
e f g

A includes 16 subsets of B.
Find the B with the biggest sum.

~ Just 4x4 iterations?

~ Example of "None" assignment.

"""


if __name__ == '__main__':
    a = []

    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))

    sum_max, sum_temp = None, None
    for i in range(4):
        for j in range(4):
            sum_temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            if sum_max is None:
                sum_max = sum_temp
            if sum_temp > sum_max:
                sum_max = sum_temp
            else:
                continue
    print(sum_max)
