import os
import json


class FileHandler:
    def read_file(self, file_name: str) -> [None, list, str]:
        if not os.path.exists(file_name):
            print("Plik o podanej nazwie nie istnieje")

            return None

        try:
            """We check if the file has a json extension, if not, we download the data as if to encrypt it"""
            _, ext = os.path.splitext(file_name)
            with open(file_name, "r", encoding="utf-8") as f:
                if ext.lower() == ".json":
                    data = json.load(f)

                    return data
                else:
                    data = f.read()

                    return data

        except Exception as e:
            print(f"Błąd podczas odczytu pliku: {e}")

            return None

