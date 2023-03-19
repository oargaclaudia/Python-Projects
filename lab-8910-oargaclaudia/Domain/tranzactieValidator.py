from datetime import datetime

from Domain.tranzactie import Tranzactie


class TranzactieValidator:
    def valideaza(self, tranzactie: Tranzactie):
        try:
            datetime.strptime(tranzactie.datasiora, '%d.%m.%Y %H:%M')
        except ValueError:
            raise ValueError("Formatul datei trebuie sa fie: DD.MM.YYYY H:M")
