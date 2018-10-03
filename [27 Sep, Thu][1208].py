# https://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python
# https://docs.python.org/3/library/fileinput.html
# import fileinput
# import sys


#
# for line in fileinput.input():
#     print(line)
#


# def read_in():
#     lines2 = sys.stdin.readlines()
#     for j in range(len(lines)):
#         lines[j] = lines[j].replace('\n', '')
#     # print lines
#     return lines2
#

# reads multiple lines and prints

lines = ""
for i in range(5):
    lines += input() + "\n"
print(lines)

#win:

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = 5
d2 = 5.0
s2 = "HackerRankRocks!"
# Read and save an integer, double, and String to your variables.

i += int(input())
d += float(input())
s += str(input())
# Print the sum of both integer variables on a new line.
print(i)
# Print the sum of the double variables on a new line.
print(d)
# Concatenate and print the String variables on a new line
print(s)
# The 's' variable above should be printed first.
