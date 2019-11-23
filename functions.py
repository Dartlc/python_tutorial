"""
    function or methods
"""

input_1 = int(input("Enter the value of input_1: "))
input_2 = int(input("Enter the value of input_2: "))


def addition_operation():
    c = input_1 + input_2
    print(f"The sum of the value is: {c}")


def subtraction_operation():
    addition_operation()
    d = input_1 - input_2
    print(f"The subtraction result is: {d}")


def division_operation():
    div = input_1 / input_2
    return div


def flor_division_operation(a: int, b: int):
    result = a // b
    print(f"The flor division result is: {result}")


if __name__ == "__main__":
    subtraction_operation()
    print(division_operation())
    flor_division_operation(a=28, b=3)
