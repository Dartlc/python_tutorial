"""
    reverse the number using for loop
"""

input_1 = int(input("Enter the start range: "))
input_2 = int(input("Enter the end range: "))

for i in range(input_1, input_2):
    rev = 0
    while i > 0:
        temp = i % 10
        rev = rev * 10 + temp
        i //= 10
    print(f"The number has been reversed {rev}")
