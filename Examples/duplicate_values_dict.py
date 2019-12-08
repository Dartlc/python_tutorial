d_1 = {'a': 10, 'b': 20, 'c': 10}
d_2 = {'a': 10, 'b': 20, 'c': 30}

input_list = list(d_1.values())
for i in d_1.values():
    if i in input_list:
        print("I found the result")
        break
    else:
        print("Not Found")
