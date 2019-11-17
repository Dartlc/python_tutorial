"""
    python has two primitive loops
        * while
        * for loop
"""

"""
    While loop
"""
num = int(input("Enter the num value: "))

while num <= 10:
    print(f"The output is {num}")
    num += 1

"""
    for loop
"""

start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))

for i in range(start_range, end_range):
    print(f"The output is {i}")

"""
    for loop increment
"""
increment = int(input("Enter the increment value: "))
for i in range(start_range, end_range, increment):
    print(f"The output is {i}")
