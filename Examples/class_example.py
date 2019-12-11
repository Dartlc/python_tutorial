"""
    class & objects
"""


class DemoClass:
    a = 0
    b = 0
    c = 0

    def add(self):
        self.c = self.a + self.b
        print(self.c)

    def odd_even(self):
        self.c = int(input("Enter the c value"))
        if self.c % 2 == 0:
            x = self.c
        else:
            x = self.c

        return x
