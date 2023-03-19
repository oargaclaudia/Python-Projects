from Domain.entitate import Entitate
from Repository.repository import Repository


# implementez interfata


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, idEntitate=None):

        if idEntitate is None:
            return list(self.entitati.values())
        if idEntitate in self.entitati:
            return self.entitati[idEntitate]
        else:
            return None

    def adauga(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is not None:
            raise KeyError("Entitatea cu id-ul pe care "
                           "noi l-am dat exista deja!")
        else:
            self.entitati[entitate.idEntitate] = entitate

    def sterge(self, idEntitate: str):
        if self.read(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate "
                           "cu id-ul dat de utilizator!")
        del self.entitati[idEntitate]

    def modifica(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is None:
            raise KeyError("Nu exista nicio entitate"
                           " cu id-ul dat de utilizator!")
        self.entitati[entitate.idEntitate] = entitate
