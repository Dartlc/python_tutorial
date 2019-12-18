"""
    global variable
    local variable
"""


def get_input():
    global a
    try:
        a = int(input("Enter the value"))
    except:
        print("Enter correct value")
        get_input()
    print(a+1)


if __name__ == '__main__':
    get_input()
