# 1) My terrible solution: --------------------------------------- #
def say_hi1(name: str, age: int) -> str:
    hi = ["Hi. My name is ", name, " and I'm ", str(age), " years old"]
    return ''.join(hi)


# 2) string built-in operation --------------------------------------- #
def say_hi(name: str, age: int) -> str:
    return "Hi. My name is %s and I'm %d years old" % (name, age)


# 3) .format --------------------------------------- #
def say_hi2(name: str, age: int) -> str:
    return "Hi. My name is {1} and I'm {0} years old".format(age, name)
    # OR 3.1: dictionary args by name
    #   person = {'name': 'Eric', 'age': 74}
    #   return "Hi. My name is {name} and I'm {age} \\
    #   \\ years old".format(name=person['name'], age=person['age'])
    #       OR 3.1.1: unpack dictionary
    #           .format(**person)


# 4) f-strings --------------------------------------- #
person = {'name': 'Eric', 'age': 74}
a = f"Hi. My name is {name} and I'm {age} years old"
b = f"{10 + 5}"
lol = "LOL"
c = f"{lol.lower()} is lowercase."
