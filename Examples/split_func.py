input_value = "name:sudhagar age:29 email:sudhagar@gmail.com"

x = input_value.split(" ")
dict_1 = {}
for i in x:
    output = i.split(":")
    dict_1[output[0]] = output[1]
print(dict_1)

result = dict(i.split(":") for i in input_value.split(" "))
print(result)
