"""
    string manipulation
"""

a = "hello world"
print(a[0])

"""
    find length
"""

word = "welcome!!"
print(len(word))

"""
    slicing
"""

input_value = "hello world"
output_1 = input_value[0:4]
output_2 = input_value[2:4]
reverse = input_value[::-1]
output_3 = input_value[3:-6]
print(output_1)
print(output_2)
print(reverse)
print(output_3)

input_2 = "Today is heavy rain"
output_4 = input_2[0:4]
output_5 = input_2[2:-3:4]
print(output_4)
print(output_5)

