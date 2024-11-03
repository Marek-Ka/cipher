from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass


class Rot13(Rot):
    def encrypt(self, text: str) -> str:
        result = ''
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += char
        return result

    def decrypt(self, text: str) -> str:
        """rot13 is symmetric"""
        return self.encrypt(text)


class Rot47(Rot):
    def encrypt(self, text: str) -> str:
        result = ''
        for char in text:
            ascii_code = ord(char)
            if 33 <= ascii_code <= 126:
                result += chr(33 + ((ascii_code + 14) % 94))
            else:
                result += char
        return result

    def decrypt(self, text: str) -> str:
        """rot47 is symmetric"""
        return self.encrypt(text)
