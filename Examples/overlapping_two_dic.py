d_1 = {"1": 2, "2": "w", "3": "q"}
d_2 = {"1": 2, "different": "w", "3": "q"}
output = []
for i in d_1:
    if i in d_2.keys():
        output.append(i)
print(output)
