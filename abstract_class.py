from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def wild(self):
        pass


class Dog(Animals):
    def wild(self):
        print("Bark, bark....")


class Elphent(Dog):
    def trunk(self):
        print("long")


obj = Elphent()
obj.wild()
obj.trunk()
