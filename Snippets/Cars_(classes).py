class Car:
    def __init__(self, color="undefined", type="undefined"):
        self.color = color
        self.type = type


def PrintCarColorAndType(obj: Car):
    print("Class '%s' has '%s' color and type '%s'." % (obj.__class__.__name__, obj.color, obj.type))


car1 = Car("blue")  # Note: you should not pass self parameter explicitly, only color parameter
car2 = Car("red", "minivan")

print("Car 1 color is %s." % car1.color)
print("Car 2 color is %s." % car2.color)
print("Car 1 type is %s." % type(car1).__name__)

PrintCarColorAndType(car2)
# It's tricky to get variable's name in Python; you should use dictionaries instead to store such data.
