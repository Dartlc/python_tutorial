input_value = int(input("Enter the number"))
sum_1 = 0

while input_value != 0:
    temp = input_value % 10
    sum_1 = sum_1 + temp
    input_value //= 10
print(sum_1)
