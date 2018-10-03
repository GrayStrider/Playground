def print_a_staircase_of_size_n(n):
    iteration = 0
    for i in range(n):
        iteration += 1
        # print(iteration)
        for j in range(n - iteration):
            print(" ", end="")
        for k in range(iteration):
            print("#", end="")
        print("\n", end="")


# print_a_staircase_of_size_n(5)


def min_Max_Sum(arr):
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum += arr[i]
        print(arr_sum)


#min_Max_Sum([1,3,5,6,7])


def all_sums(arr):  # for  len(arr) numbers.
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)


#all_sums([1,2,3,4])


def all_sums(arr):  # all sums with 2 numbers. WORKS DON'T DELETE
    for i in range(len(arr)):
        for j in range(len(arr)):
            if id(arr[i]) != id(arr[j]):  # don't sum with itself
                sum = arr[i] + arr[j]
                print(sum)


#all_sums([1,2,3])


def all_sums(arr):  # don't go back while iterating
    for i in range(len(arr) - 1):
        print("iteration i: " + str(i))
        for j in range(len(arr) - 1 + 1):
            print("iteration j: " + str(j))
            sum = arr[i] + arr[(i+1):]
            print(str(sum))


all_sums([1,2,3,4,5])

def all_sums(arr):  # don't go back while iterating
    for i in range(4):
        print("iteration i: " + str(i))
        for j in range(3):
            print("iteration j: " + str(j))
            sum = arr[i] + arr[i + 1]
            print(str(sum))


#all_sums([1,2,3,4,5])
