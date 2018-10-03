"""

Reads n lines from user input, followed by Enter,
then prints.

"""

n = 5
lines = ""
for i in range(n):
    lines += input() + "\n"
print(lines)
