def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


num = 1004


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')


print(expanded_form(num))
