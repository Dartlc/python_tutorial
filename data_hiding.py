class DataHiding:
    def __init__(self):
        self.__a = 20
        self.b = 30

    def result(self):
        print(self.__a)


if __name__ == '__main__':
    obj = DataHiding()
    obj.result()

    print(obj.__a)
