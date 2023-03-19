from datetime import datetime
from Domain.card import Card


class CardValidator:
    def valideaza(self, card: Card):
        try:
            datetime.strptime(card.datanasterii, '%d.%m.%Y')
            datetime.strptime(card.datainregistrarii, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Formatul datei trebuie sa fie: DD.MM.YYYY")
