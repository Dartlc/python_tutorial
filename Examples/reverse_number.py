"""
    reverse the number using while loop
"""
input_1 = int(input("Enter the number to reverse: "))
rev = 0

while input_1 > 0:
    temp = input_1 % 10
    rev = rev * 10 + temp
    input_1 //= 10

print(f"The number has been reversed {rev}")
