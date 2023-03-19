from Domain.masina import Masina
from Domain.masinaError import MasinaError


class MasinaValidator:
    def valideaza(self, masina: Masina):
        erori = []
        if masina.nrKmMasina <= 0:
            erori.append("Numarul de km trebuie sa fie strict pozitiv !")
        if masina.anAchizitie <= 0:
            erori.append("Anul achizitiei trebuie sa fie strict pozitiv !")
        if len(erori) > 0:
            raise MasinaError(erori)
