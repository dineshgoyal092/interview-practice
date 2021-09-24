# from abc import ABC, abstractmethod ##python 3
import abc

class AbstractClassExample(metaclass=abc.ABCMeta):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class temp(AbstractClassExample):
    def do_something(self):
        print(self.value)

a = temp(10)
a.do_something()
