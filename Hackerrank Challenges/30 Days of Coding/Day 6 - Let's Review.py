# string = str(input())
#
# i = 0
# while i in range(len(string)):
#     if i % 2 == 0:
#         print(string[i], end="")
#     i += 1
#
# print(" ")
#
# i = 0
# while i in range(len(string)):
#     if i % 2 != 0:
#         print(string[i], end="")
#     i += 1
#
# exit()
#

# git gud?
# git gud scrub [16:12]

t = int(input())
for i in range(0, t):
    print("waiting for input")
    string = str(input())

    i = 0
    while i in range(len(string)):
        if i % 2 == 0:
            print(string[i], end="")
        i += 1

    print(" ", end="")

    i = 0
    while i in range(len(string)):
        if i % 2 != 0:
            print(string[i], end="")
        i += 1
    print("")

exit()


"""
2
test
what

"""
