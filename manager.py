import sys
from beaupy import confirm
from menu import Menu
from file_handler import FileHandler
from cipher import Rot13, Rot47
from buffer import Buffer
from text_obj import Text

class Manager:
    def __init__(self):
        self.menu = Menu()
        self.file_handler = FileHandler()
        self.rot13, self.rot47 = Rot13(), Rot47()
        self.buffer = Buffer()

    def run(self):
        while True:
            choice = self.menu.main_menu_choice()
            match choice:
                case "Zaszyfruj dane":
                    self.cipher_text("encrypted")
                case "Odszyfruj dane":
                    self.cipher_text("decrypted")
                case "Zapisz do pliku":
                    self.save_to_file()
                case "Odczytaj z pliku":
                    self.load_from_file()
                case "Pokaż wykaz dzisiejszych operacji":
                    print(self.buffer.get_all_buffer())
                case "Zakończenie programu":
                    sys.exit("Wybrane zakończenie działania programu")
                case _:
                    sys.exit("Nieprawidłowa opcja - zakończenie działania programu")

    def prepare_cipher_json_data(self, data, status):
            cipher_text = ""
            rot_type = self.menu.rot_menu_choice()
            match rot_type:
                case "rot13":
                    if status == "decrypted":
                        cipher_text = self.rot13.decrypt(data)
                    else:
                        cipher_text = self.rot13.encrypt(data)
                case "rot47":
                    if status == "decrypted":
                        cipher_text = self.rot47.decrypt(data)
                    else:
                        cipher_text = self.rot47.encrypt(data)

            text_obj = (Text(text=cipher_text, rot_type=rot_type, status=status))
            text_json = vars(text_obj)

            return text_json

    def cipher_text(self, status):
        source = self.menu.source_menu_choice()
        match source:
            case "Dane z pliku":
                file_name = input("Podaj nazwę pliku do zaczytania danych: ")
                data = self.file_handler.read_file(file_name)
                if confirm("Czy rozbić dane na linie?"):
                    data = data.split("\n")
                    for line in data:
                        text_json = self.prepare_cipher_json_data(line, status)
                        self.buffer.add_buffer(text_json)
                else:
                    text_json = self.prepare_cipher_json_data(data, status)
                    self.buffer.add_buffer(text_json)

            case "Dane wprowadzone ręcznie":
                data = input("Wprowadź tekst do zaszyfrowania: ")
                text_json = self.prepare_cipher_json_data(data, status)
                self.buffer.add_buffer(text_json)

    def save_to_file(self) -> None:
        file_name = input("Podaj nazwę pliku z rozszerzeniem '.json': ")
        data = self.buffer.get_all_buffer()
        self.buffer.clear_buffer()
        self.file_handler.write_file(file_name, data)

    def load_from_file(self):
        file_name = input("Podaj nazwę pliku do odczytu: ")
        data = self.file_handler.read_file(file_name)
        if data:
            if isinstance(data, list):
                for position in data:
                    print(position)
            else:
                print(data)
