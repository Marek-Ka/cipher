class Buffer:
    def __init__(self):
        self.buffer_list = []

    def add_buffer(self, text_json) -> None:
        self.buffer_list.append(text_json)

    def get_all_buffer(self) -> [str, list]:
        if len(self.buffer_list) < 1:
            return "Nie przesłałeś jeszcze żadnych danych do szyfrowania."

        return self.buffer_list

    def clear_buffer(self) -> None:
        self.buffer_list = []
