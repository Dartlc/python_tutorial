"""
    file handling
"""
f = open("list_file.txt", "w")
a = []
dict_1 = {"hello": "world"}
for i in range(10, 20):
    a.append(i)
f.write(f"{a}")
f.write(f"{dict_1}")
f.close()
