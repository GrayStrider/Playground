"""

[Time Conversion]

12:05:45AM
10:05:45AM

>> 07:05:45PM
>> 19:05:45

"""


def timeConversion(s):

    time12 = list(s)
    time24 = []

    # AM
    if time12[-2:] == ["A", "M"]:

        # AM and 12
        if time12[:2] == ["1", "2"]:
            time24[:2] = ["0", "0"]
            time24 = time24 + (time12[2:8])
            return ''.join(time24)

        # AM not 12
        time24 = time24 + (time12[:8])
        return ''.join(time24)

    # PM
    else:

        # PM and 12
        if time12[:2] == ["1", "2"]:
            time24[:2] = ["1", "2"]
            time24 = time24 + (time12[2:8])
            return ''.join(time24)

        hours24 = int(s[:2]) + 12
        hours24 = str(hours24)

        temp = [0,0]
        temp[:] = hours24[:]

        time24 = temp + (time12[2:8])
        return ''.join(time24)


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
