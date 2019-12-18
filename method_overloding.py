"""
    same function name different parameters
"""


def demo(a, b):
    c = a + b
    print(c)


def demo(a, b, c):
    c = a + b + c
    print(c)


"""
    args and kwargs
"""


def sample(*args):
    for i in args:
        print(i)


if __name__ == '__main__':
    demo(a=5, b=6, c=10)
    sample(20, 21, 32, 43, 23, 54, 62)
