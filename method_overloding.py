"""
    same function name different parameters
"""

"""
    args and kwargs
"""


def sample(*args):
    for i in args:
        print(i)


if __name__ == '__main__':
    sample(20, [1, 2, 3, 4, 5, 6, 7, 6], "sudhagar")
