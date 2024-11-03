from beaupy import *


class Menu:
    def __init__(self):
        self.main_menu = [
            "Zaszyfruj dane",
            "Odszyfruj dane",
            "Zapisz do pliku",
            "Odczytaj z pliku",
            "Pokaż wykaz dzisiejszych operacji",
            "Zakończenie programu"
        ]
        self.source_menu = [
            "Dane z pliku",
            "Dane wprowadzone ręcznie"
        ]
        self.rot_menu = [
            "rot13",
            "rot47"
        ]

