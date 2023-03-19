from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiDelete(UndoRedoOperation):
    def __init__(self, repository_1: Repository, repository_2:
                 Repository, obiecte_sterse_1, obiecte_sterse_2):
        self.repository_1 = repository_1
        self.repository_2 = repository_2
        self.obiecte_sterse_1 = obiecte_sterse_1
        self.obiecte_sterse_2 = obiecte_sterse_2

    def doUndo(self):
        for entitate in self.obiecte_sterse_1:
            self.repository_1.adauga(entitate)

        for entitate in self.obiecte_sterse_2:
            self.repository_2.adauga(entitate)

    def doRedo(self):
        for entitate in self.obiecte_sterse_1:
            self.repository_1.sterge(entitate.idEntitate)

        for entitate in self.obiecte_sterse_2:
            self.repository_2.sterge(entitate.idEntitate)
