def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


text = "ZpglnRxqenU"
print(accum(text))
print([[l, c] for l, c in enumerate(text)])
# Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu
# [[0, 'Z'], [1, 'p'], [2, 'g'], [3, 'l'], [4, 'n'], [5, 'R'], [6, 'x'], [7, 'q'], [8, 'e'], [9, 'n'], [10, 'U']]
