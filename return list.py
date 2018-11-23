def compare(a: int, b: int):
    return [f"{a} is less than {b}",
            f"{a} is more than {b}",
            f"{a} is equal to {b}"] \
        [0 if a < b else 1 if a > b else 2]


print(compare(11, 10))
