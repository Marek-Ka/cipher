from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass


