from dataclasses import dataclass

from Domain.tranzactie import Tranzactie
from Domain.masina import Masina


@dataclass
class OrdonareManoperaViewModel:
    tranzactie: Tranzactie
    masina: Masina

    def __str__(self):
        return f'{self.masina} \n\tcu tranzactia {self.tranzactie}'
