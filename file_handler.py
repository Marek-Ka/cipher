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

    def write_file(self, file_name: str, data: list) -> None:
        try:
            if os.path.exists(file_name):
                with open(file_name, "r+", encoding="utf-8") as f:
                    try:
                        existing_data = json.load(f)
                        if isinstance(existing_data, list):
                            existing_data.extend(data)
                        else:
                            existing_data = [existing_data] + data
                    except json.JSONDecodeError:
                        existing_data = data
                    f.seek(0)
                    json.dump(existing_data, f, ensure_ascii=False, indent=4)
            else:
                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Błąd podczas zapisu do pliku: {e}")
