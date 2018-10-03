def sum1(arr):
    sum = 0
    for row in range (len(arr)):
        for col in range(len(arr[0])):
            sum = sum + arr[row][col]
            print(sum)

    return sum

a = [[1, 2],[3, 4],[5, 6]]
sum1(a)

print(len(a))
print(type(len(a)))
print(type(a))

b = [1,2,3]

for i in b:
    print(i)
    print(b.index(i))

print(range(2))
print("#############\n")

c = [100, 10, 12]
sum = 1

for i in range(len(c)):
    sum += c[i]
print(sum)
