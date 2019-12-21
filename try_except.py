"""
    Error Handling.
        try, except
"""

"""
    Validate input values by using try & except
"""

try:
    a = int(input("Enter the 'a' value: "))
    b = int(input("Enter the 'b' value: "))

except:
    print("The 'a' and 'b' must integer.")

try:
    a = int(input("Enter the 'a' value: "))
    b = int(input("Enter the 'b' value: "))
    c = d

except NameError as e:
    print(f"{e}")

try:
    e = f
except Exception as e:
    print(f"{e}")

finally:
    print("bye")

try:
    input_value = int(input("enter the input value: "))
    input_value_2 = int(input("enter the input value: "))
except Exception as e:
    print(f"{e}")

if input_value % 2 == 0:
    print("Even")