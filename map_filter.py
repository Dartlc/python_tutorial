# map function

a = ["Hello", "world", "welcome"]


def length_of_each_elements(n):
    return len(n)


x = map(length_of_each_elements, a)
print(list(x))


# filter function

def filter_the_values_using_filter_function(x):
    if x == "world":
        return True


x = filter(filter_the_values_using_filter_function, a)
print(list(x))
