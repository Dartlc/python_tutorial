"""
    class and objects
"""


class Demo:

    def odd_even(self):
        self.value = 153

        if self.value % 2 == 0:
            print("Even")
        else:
            print("Odd")


if __name__ == '__main__':
    obj = Demo()
    obj.odd_even()
