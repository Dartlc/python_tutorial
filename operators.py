"""
    python has 7 types of operators

    1. arithmetic operators
    2. assignment operators
    3. comparison operators
    4. logical operators
    5. identity operators
    6. membership operators
    7. bitwise operators

"""

"""
    Arithmetic operators
        addition - '+'
        subtraction - '-'
        Division - '/'
        multiplication - '*'
        modulus - '%'
        exponential - '**'
        floor division - '//' 
        
"""
a = 15  # Variable initiation
b = 3

"""
    addition operators
"""
c = a + b
print(f"The addition of two number is {c}")  # Addition result for two number

"""
    subtraction operators
"""
c = a - b
print(f"The subtraction of two number is {c}")  # Subtraction result for two numbers

"""
    multiplication operators
"""
c = a * b
print(f"The multiplication of two number is {c}")  # Multiplication result for two numbers

"""
    Division operators
"""
c = a / b
print(f"The Division of two number is {c}")  # Division result for two numbers

"""
    modulus operator
"""
c = a % b
print(f"The modulus of two number is {c}")  # The result will be a remainder of divided operation

"""
    exponential operator
"""
c = a ** b
print(
    f"The exponential of two number is {c}")  # The result will be calculate the exponential value with the base set to e.

"""
    floor division
"""
c = a // b
print(f"The floor division of two number is {c}")  # Returns the integral part of the quotient.

"""
    Assignment operators
"""
a = 15

a += 3  # a = a + 3
print(f"The result will be incremented by 3 {a}")  # The result will be incremented by 3

a -= 3  # a = a - 3
print(f"The result will be decremented by 3 {a}")  # The result will be decremented by 3

a *= 3  # a = a * 3
print(f"The result will be multiplied by 3 {a}")  # The result will be multiplied by 3

a /= 3  # a = a / 3
print(f"The result will be divided by 3 {a}")  # The result will be divided by 3

a %= 3  # a = a % 3
print(f"The remainder will be {a}")  # The result will be a remainder of divided operation

a **= 3  # a = a ** 3
print(
    f"The result will be {a}")  # The result will be calculate the exponential value with the base set to e.

a //= 3  # a = a // 3
print(f"The result will be {a}")  # Returns the integral part of the quotient.

"""
    comparison operators
"""

"""
    Equal
"""
a = 10
b = 5
c = a == b
print(f"The comparison between a and b is {c}")  # The Result will be in boolean format

"""
    Not equal
"""
c = a != b
print(f"The comparison between a and b is {c}")  # The Result will be in boolean format

"""
    Less than
"""
c = a < b
print(f"The comparison between a and b is {c}")  # The Result will be in boolean format

"""
    Greater than
"""
c = a > b
print(f"The comparison between a and b is {c}")  # The Result will be in boolean format

"""
    Less than or equal
"""
c = a <= b
print(f"The comparison between a and b is {c}")  # The Result will be in boolean format

"""
    Greater than or equal
"""
c = a >= b
print(f"The comparison between a and b is {c}")  # The Result will be in boolean format

"""
    logical operators
"""
x = 20

"""
    and operator
"""
result = x > 10 and x < 30  # Compare the values by using and operator
print(f"The result will be {result}")

"""
    or operator
"""
result = x > 10 or x < 10  # Compare the values by using and operator
print(f"The result will be {result}")

"""
    not operator
"""

result = not(x > 10 and x < 30)   # Compare the values by using and operator
print(f"The result will be {result}")

"""
    identity operators
"""

"""
    is operator
"""

output = result is True
print(f"The output is {output}")

"""
    is not operator
"""

output = result is not True
print(f"The output is {output}")

"""
    membership operator
"""
name = "Hello World"

"""
    in operator
"""
result = "o" in name
print(f"The result will be {result}")

"""
    not in
"""
result = 'o' not in name
print(f"The result will be {result}")

