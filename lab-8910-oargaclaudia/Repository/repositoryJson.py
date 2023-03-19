import jsonpickle

from Domain.entitate import Entitate
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readfile(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writefile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati, indent=2))

    def read(self, idEntitate=None):
        self.entitati = self.__readfile()
        # se duce la metoda read a clasei de baza
        return super().read(idEntitate)

    def adauga(self, entitate: Entitate):
        self.entitati = self.__readfile()
        super().adauga(entitate)
        self.__writefile()

    def sterge(self, idEntitate):
        self.tranzactii = self.__readfile()
        super().sterge(idEntitate)
        self.__writefile()

    def modifica(self, entitate: Entitate):
        self.tranzactii = self.__readfile()
        super().modifica(entitate)
        self.__writefile()
