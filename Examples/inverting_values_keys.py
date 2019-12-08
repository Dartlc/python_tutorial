output = {}
input_value = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
values = input_value.items()
for key, value in values:
    output[value] = key
print(output)
