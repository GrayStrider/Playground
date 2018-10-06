"""

1) Convert n to binary
    divide by 2, push the reminder to a stack
    test: convert back to decimal
        (xyn)_2 -> (z)_10 = (x * 2^2) + (y * 2^1) + (n * 2^(n-1))
2) Print the biggest streak of 1s.


! - reverse the string through extended slice syntax
"""


# Works.
def dec_to_bin(n):
    bin = ""
    while n > 0:
        bin += str(n % 2)
        n = int(n / 2)
    bin = bin[::-1]
    return bin


# NOT working.
def bin_to_dec(n):
    dec = 0
    bin = str(n)
    for i in reversed(range(len(bin))):
        dec += int(bin[i]) * (2 ^ i)
        print("Count = %d" % i)
        print("Dec = %d" % dec)
    return dec


def day10(n):
    max, max_temp = 0, 0
    n = list(dec_to_bin(n))
    for i in range(len(n)):
        if n[i] == "1":
            max_temp += 1
            if max_temp > max:
                max = max_temp
        else:
            max_temp = 0
    return max


n = 456
print(dec_to_bin(n))
print(day10(n))
