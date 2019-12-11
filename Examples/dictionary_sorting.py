"""
    dictionary sorting
"""

input_value = {10: 20, 1: 11, 12: 23, 13: 43, 100: 234, 111: 21, 432: 342}  # input dictionary

"""
    sort by key using sort function, ascending order 
"""
x = dict(sorted(input_value.items()))
print(x)

"""
    sort by key using sort function, descending order
"""
x = dict(sorted(input_value.items(), reverse=True))
print(x)

"""
    sort by key using dictionary comprehension, ascending order
"""

y = {k: v for k, v in sorted(input_value.items())}
print(y)

"""
    sort by key using dictionary comprehension, descending order
"""

y = {k: v for k, v in sorted(input_value.items(), reverse=True)}
print(y)

"""
    sort by value using sort function and lambda function, ascending order
"""

y = dict(sorted(input_value.items(), key=lambda kv: (kv[1], kv[0])))
print(y)

"""
    sort by value using sort function and lambda function, descending order
"""

y = dict(sorted(input_value.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
print(y)


