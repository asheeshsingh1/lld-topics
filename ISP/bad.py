from abc import ABC, abstractmethod

# Abstract Base Class in Python
class UberUser(ABC):

    @abstractmethod
    def bookRide(self):
        pass

    @abstractmethod
    def acceptRide(self):
        pass

    @abstractmethod
    def trackEarnings(self):
        pass

    @abstractmethod
    def ratePassenger(self):
        pass

    @abstractmethod
    def rateDriver(self):
        pass
