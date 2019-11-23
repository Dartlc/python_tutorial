"""
    Control statements
        => break
        => continue
        => pass
"""

"""
    break statements
"""

a = "sudhagar"
for i in a:
    if i == "a":
        break
    print(i)


"""
    continue statements
"""

x = "hello world"
count = 0
for i in x:
    if i == "o":
        count += 1
        print("hello world")
        continue
    print(i)

print(count)

"""
    pass statement
"""

for i in "hello world":
    if i == "o":
        pass
    print(i)
