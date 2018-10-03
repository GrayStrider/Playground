"""

Prints a staircase of size n.

"""


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


# version 2.0, thanks Dork for believing in me
def print_a_staircase_of_size_n(n):
    a = n
    for i in range(n):
        print((" " * (a - 1)) + ("#" * (i + 1)))
        a -= 1


print_a_staircase_of_size_n(5)
