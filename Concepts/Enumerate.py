def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum("ZpglnRxqenU"))


# Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu

def foo(s):
    return "".join(str(i) + c for i, c in enumerate(s))


print(foo("ZpglnRxqenU"))

dict = {"1": "test", "2": "another"}

print(foo(dict))
