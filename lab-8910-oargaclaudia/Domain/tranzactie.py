from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Tranzactie(Entitate):
    idmasina: str
    idcardclient: str
    sumapiese: float
    sumamanopera: float
    datasiora: str
