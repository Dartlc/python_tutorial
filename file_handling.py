import os
"""
    file mode has four types
    1. create mode - 'x'
    2. read mode - 'r'
    3. write mode - 'w'
    4. append mode - 'a'
"""
"""
    file creating
"""
try:
    f = open("sample.txt", "x")
    f.close()
except Exception as e:
    print(e)


""" 
    create a file and write in file
"""

f = open("/home/sudhagar/Desktop/test/demo.txt", "w")
f.write("hello world!!! welcome")
f.close()

"""
    read a file
"""

f = open("demo.txt", "r")
x = f.read()
print(x)
f.close()

"""
    append the data into the file
"""

f = open("/home/sudhagar/Desktop/test/demo.txt", "a")
f.write("\nhave a nice day")
f.close()

"""
    Delete file
"""

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
