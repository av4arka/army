from abc import ABCMeta, abstractmethod

class Observable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass
