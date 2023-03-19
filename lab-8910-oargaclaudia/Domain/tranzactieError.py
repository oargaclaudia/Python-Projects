from dataclasses import dataclass


@dataclass
class TranzactieError(Exception):
    mesaj: str

    def __str__(self):
        return f'TranzactieError: {self.mesaj}'
