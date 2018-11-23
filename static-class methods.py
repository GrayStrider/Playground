class Test:
    a = 10

    def __init__(self):
        self.a = 15

    @staticmethod
    def staticMethod(num: int):
        a = 5
        print(a + num)

    @classmethod
    def classMethod(cls, num: int):
        print(cls.a + num)
        print(Test.a + num)

    def justMethod(self, num: int):
        self.a = 5
        print(self.a + num)


# does not require instantiating.
Test.staticMethod(10)  # 5
Test.classMethod(10)  # 20

objTest = Test()  # a == 15
objTest.justMethod(10)  # 15
