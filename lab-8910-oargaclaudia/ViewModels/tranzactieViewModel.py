from Domain.card import Card
from Domain.masina import Masina


class TranzactieViewModel:
    def __init__(self, id_tranzactie, masina: Masina,
                 card_client: Card, sumapiese,
                 sumamanopera, data_ora):
        self.id_tranzactie = id_tranzactie
        self.masina = masina
        self.card_client = card_client
        self.sumapiese = sumapiese
        self.sumamanopera = sumamanopera
        self.data_ora = data_ora

    def __str__(self):
        return f'id tranzactie:{self.id_tranzactie} \n-------cu masina ' \
               f'{self.masina} \n-------si card_client {self.card_client},' \
               f'suma piese: {self.sumapiese},' \
               f' suma manopera: {self.sumamanopera},' \
               f'data si ora: {self.data_ora} '
