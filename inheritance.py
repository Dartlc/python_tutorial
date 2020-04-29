"""
    three types of inheritance
    1) single inheritance.
    2) multiple inheritance
    3) multilevel inheritance
"""

"""
    single inheritance
    
        definition: A base class have a single derived class its called single inheritance.
"""


class Biggest:
    def __init__(self):
        self.a = int(input("Enter the 'a' value: "))
        self.b = int(input("Enter the 'b' value: "))

    def display(self):
        if self.a > self.b:
            print("the biggest value is 'a' {}".format(self.a))
        else:
            print("The biggest value is 'b' {}".format(self.b))


class Reverse(Biggest):
    def __init__(self):
        super().__init__()
        self.c = self.a + self.b
        self.reverse = 0
        self.temp = 0

    def display_1(self):
        while self.c > 0:
            self.temp = self.c % 10
            self.reverse = self.reverse * 10 + self.temp
            self.c = self.c // 10
        print("The reversed number is {}".format(self.reverse))


if __name__ == '__main__':
    obj = Reverse()
    obj.display()
    obj.display_1()

"""
    multilevel inheritance
        definition: A base class have a derived class and the derived class will act as a base class of another derived 
                    class, then its called multilevel inheritance. 
"""


class Biggest:
    def __init__(self):
        self.a = int(input("Enter the 'a' value: "))
        self.b = int(input("Enter the 'b' value: "))

    def display(self):
        if self.a > self.b:
            print("the biggest value is 'a' {}".format(self.a))
        else:
            print("The biggest value is 'b' {}".format(self.b))


class Reverse(Biggest):
    def __init__(self):
        super().__init__()
        self.c = self.a + self.b
        self.reverse = 0
        self.temp = 0

    def display_1(self):
        while self.c > 0:
            self.temp = self.c % 10
            self.reverse = self.reverse * 10 + self.temp
            self.c = self.c // 10
        print("The reversed number is {}".format(self.reverse))


class OddEven(Reverse):
    def __init__(self):
        super().__init__()
        self.d = self.a + self.b

    def display_2(self):
        if self.d % 2 == 0:
            print("even")
        else:
            print("odd")


if __name__ == '__main__':
    obj = OddEven()
    obj.display()
    obj.display_1()
    obj.display_2()

"""
    multiple inheritance
        definition: A multiple base class have a single derived class its called multilevel inheritance 
"""


class Animal:
    def display_1(self):
        print(f"Their are two kind of animals")


class Dog:
    def display_2(self):
        print(f"Dog is domestic animal")


class Parrot:
    def display_3(self):
        print(f"parrot is bird")


class Result(Animal, Dog, Parrot):
    def display_4(self):
        super().__init__()
        print(f"The result")


if __name__ == '__main__':
    obj = Result()
    obj.display_4()
    obj.display_1()
    obj.display_2()
    obj.display_3()
