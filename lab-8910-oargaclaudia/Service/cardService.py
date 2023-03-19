from Domain.addOperation import AddOperation
from Domain.cardValidator import CardValidator
from Domain.card import Card
from Domain.deleteOperation import DeleteOperation
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class CardService:
    def __init__(self, cardRepository: Repository,
                 cardValidator: CardValidator,
                 undoRedoService: UndoRedoService):
        self.__cardRepository = cardRepository
        self.__cardValidator = cardValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__cardRepository.read()

    def adauga(self, idcard, nume,
               prenume, CNP,
               datanasterii,
               datainregistrarii):
        for card in self.__cardRepository.read():
            if CNP == card.CNP:
                raise KeyError("CNP-ul exista deja!")
        card = Card(idcard, nume, prenume,
                    CNP, datanasterii,
                    datainregistrarii)
        self.__cardValidator.valideaza(card)
        self.__cardRepository.adauga(card)
        self.__undoRedoService.addUndoRedoOperation(AddOperation(
            self.__cardRepository, card
        ))

    def sterge(self, idcard):
        cardulsters = self.__cardRepository.read(idcard)
        self.__cardRepository.sterge(idcard)
        self.__undoRedoService.addUndoRedoOperation(
            DeleteOperation(self.__cardRepository, cardulsters))

    def modifica(self, idcard, nume,
                 prenume, CNP,
                 datanasterii,
                 datainregistrarii):
        card_vechi = self.__cardRepository.read(idcard)
        for card in self.__cardRepository.read():
            if CNP == card.CNP:
                raise KeyError("CNP-ul exista deja!")
        card = Card(idcard, nume, prenume,
                    CNP, datanasterii,
                    datainregistrarii)
        self.__cardValidator.valideaza(card)
        self.__cardRepository.modifica(card)
        self.__undoRedoService.addUndoRedoOperation(
            ModifyOperation(self.__cardRepository, card_vechi, card))

    def cautareCardClient(self, cuvant):
        rezultat = self.__cardRepository.read()
        return list(filter(lambda x: cuvant in x.nume or
                           cuvant in x.prenume or
                           cuvant in str(x.CNP) or
                           cuvant in str(x.datainregistrarii) or
                           cuvant in str(x.datanasterii),
                           rezultat))
