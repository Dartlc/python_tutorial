"""
    file handling
"""
f = open("list_file.txt", "w")
a = []
for i in range(10, 20):
    a.append(i)
f.write(f"{a}")
