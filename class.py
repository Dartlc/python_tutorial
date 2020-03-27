"""
    class and objects
"""


class Calc:

    def addition(self, a, b):
        self.c = a + b
        print(self.c)

    def subraction(self, a, b):
        self.d = a - b
        print(self.d)


obj = Calc()
obj.addition(a=20, b=30)
obj.subraction(a=20, b=30)
