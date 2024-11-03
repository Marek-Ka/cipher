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

    def get_choice(self, options: list) -> str:
        return select(options, cursor=">>", cursor_style="cyan")

    def main_menu_choice(self) -> str:
        console.print("Wybierz opcję: ")

        return self.get_choice(self.main_menu)

    def source_menu_choice(self) -> str:
        console.print("Skąd pobrać dane do operacji?")

        return self.get_choice(self.source_menu)

    def rot_menu_choice(self) -> str:
        console.print("Podaj rodzaj szyfrowania:")

        return self.get_choice(self.rot_menu)
