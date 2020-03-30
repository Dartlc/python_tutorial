class Addition:
    def __init__(self, a, b):
        self.c = a + b
        print(self.c)

    def __del__(self):
        print("destructor is executed....")


obj = Addition(a=20, b=30)
print(id(obj))
del obj
print(id(obj))
