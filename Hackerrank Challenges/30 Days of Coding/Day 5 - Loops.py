"""

"print" formatting.

"""

if __name__ == '__main__':
    print("Enter 2 numbers, separated by space:")
    n = int(input("First number: "))
    m = int(input("Second number: "))

    for i in range(1, m+1):
        print(f"{n} * {i} = {n*i}")
