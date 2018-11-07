from abc import ABCMeta, abstractmethod

class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, observable):
        pass

    @abstractmethod
    def add_observable(self, observable):
        pass

    @abstractmethod
    def erase_observable(self, observable):
        pass