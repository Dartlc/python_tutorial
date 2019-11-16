input_1 = int(input("Enter the first input value: "))
input_2 = int(input("Enter the second value: "))
input_3 = int(input("Enter the third value: "))

"""
    if and else are condition statements
"""

if input_1 > input_2:
    print(f"The biggest value is {input_1}")
else:
    print(f"The biggest value is {input_2}")

"""
    if and elif condition statements
"""

if input_1 > input_2 and input_1 > input_3:
    print(f"The biggest value is {input_1}")
elif input_2 > input_1 and input_2 > input_3:
    print(f"The biggest value is {input_2}")
else:
    print(f"The biggest value is {input_3}")

"""
    nested if and else 
"""

if input_1 != 0 and input_2 != 0 and input_3 != 0:
    if input_1 > input_2 and input_1 > input_3:
        print(f"The biggest value is {input_1}")
    elif input_2 > input_1 and input_2 > input_3:
        print(f"The biggest value is {input_2}")
    else:
        print(f"The biggest value is {input_3}")
else:
    print(f"The input value must not be 0")