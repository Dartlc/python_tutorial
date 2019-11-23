"""
    List
"""

# list is also called a data type.It is mutable and ordered.

"""
    => List
    => list can be mutable and ordered
"""
a = []
x = [1, "sudhagar", 2, 3, 4, 5, 6, 7]

start = int(input("enter the start range: "))
end = int(input("enter the end range: "))

for i in range(start, end):
    a.append(i)  # appending values in a
print(a)

for i in a:
    if i % 2 == 0:
        print(f"This numbers are even {i}")
    else:
        print(f"This numbers are odd {i}")


"""
    => Tuple
    => Tuple is immutable and ordered
"""

a = (1, 2, 3, 4, 5, 6)
print(a)
b = ()

for i in a:
    print(i)  # iterate the values in the tuple

"""
    => Set
    => Set is un ordered
"""

a = {}
x = {1, 3, 4, 5, 8, 9, 0, 2, 3, 4, 5, 6}
print(x)

for k in x:
    print(k)  # iterate the in the set

"""
    => dict
    => dict is mutable and ordered
    => dict have a key and values
"""

dict_value = {"name_1": "sudhagar", "name": "sudhagar"}
print(dict_value)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
obj = {"key": x}
print(obj)

list_1 = []
for i in range(20, 30):
    list_1.append({i: i})
print(list_1)