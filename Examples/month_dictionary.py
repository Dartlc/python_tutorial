input_dict = {"january": "31", "august": "30", "December": 31}

key_value = []
for i in input_dict:
    key_value.append(i)
x = sorted(key_value)
print(x)

y = {k: v for k, v in sorted(input_dict.items())}
print(y)

