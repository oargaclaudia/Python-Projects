from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Masina(Entitate):
    '''
    Creeaza o masina
    idMasina: id-ul masinii. Trebuie sa fie unic
    modelMasina: Modelul masinii
    anAchizitie: Anul achizitiei masinii
    nrKmMasina: Numarul de kilometri ai masinii
    GarantieMasina:
    Informatii referitoare la garantia masinii:
    da/nu - in garantie/nu  e in garantie
    '''
    modelMasina: str
    anAchizitie: int
    nrKmMasina: float
    GarantieMasina: str
