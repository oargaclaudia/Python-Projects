import functools
from datetime import datetime
from functools import reduce

from Domain import card
from Domain.addOperation import AddOperation
from Domain.deleteMultiply import DeleteMultiply
from Domain.deleteOperation import DeleteOperation
from Domain.modifyOperation import ModifyOperation
from Domain.multiDelete import MultiDelete
from Domain.tranzactie import Tranzactie
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService
from ViewModels.ordonareManoperaViewModel import OrdonareManoperaViewModel
from ViewModels.tranzactieViewModel import TranzactieViewModel


class TranzactieService():
    def __init__(self, tranzactieRepository: Repository,
                 masinaRepository: Repository,
                 cardRepository: Repository,
                 tranzactieValidator: TranzactieValidator,
                 undoRedoService: UndoRedoService):
        self.__undoRedoService = undoRedoService
        self.__tranzactieRepository = tranzactieRepository
        self.__masinaRepository = masinaRepository
        self.__cardRepository = cardRepository
        self.__tranzactieValidator = tranzactieValidator

    def getAll(self):
        return self.__tranzactieRepository.read()

    def adauga(self, idtranzactie, idmasina,
               idcardclient, sumapiese,
               sumamanopera, datasiora):
        if self.__masinaRepository.read(idmasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__cardRepository.read(idcardclient) is None:
            raise KeyError("Nu exista niciun client cu cardul dat!")

        tranzactie = Tranzactie(idtranzactie, idmasina,
                                idcardclient, sumapiese,
                                sumamanopera, datasiora)
        self.__tranzactieValidator.valideaza(tranzactie)
        masina = self.__masinaRepository.read(idmasina)
        if masina.GarantieMasina == "da":
            tranzactie.sumapiese = 0
        # if self.__cardRepository.read(idcardclient) is not None:
        # if masina.GarantieMasina=="da":
        # tranzactie.sumamapiese = 0
        if self.__cardRepository.read(idcardclient) is not None:
            tranzactie.sumamanopera = tranzactie.sumamanopera - \
                                      tranzactie.sumamanopera / 10.0

        self.__tranzactieRepository.adauga(tranzactie)
        self.__undoRedoService.addUndoRedoOperation(
            AddOperation(self.__tranzactieRepository, tranzactie))

    def sterge(self, idtranzactie):
        tranzactie_stearsa = self.__tranzactieRepository.read(idtranzactie)
        self.__tranzactieRepository.sterge(idtranzactie)
        self.__undoRedoService.addUndoRedoOperation(
            DeleteOperation(self.__tranzactieRepository, tranzactie_stearsa))

    def modifica(self, idtranzactie, idmasina,
                 idcardclient, sumapiese,
                 sumamanopera, datasiora):
        if self.__masinaRepository.read(idmasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__cardRepository.read(idcardclient) is None:
            raise KeyError("Nu exista niciun client cu cardul dat!")
        tranzactie_veche = self.__tranzactieRepository.read(idtranzactie)
        tranzactie = Tranzactie(idtranzactie, idmasina,
                                idcardclient, sumapiese,
                                sumamanopera, datasiora)
        self.__tranzactieValidator.valideaza(tranzactie)
        masina = self.__masinaRepository.read(idmasina)
        card = self.__cardRepository.read(idcardclient)
        if masina.GarantieMasina == "da":
            tranzactie.sumapiese = 0
        if self.__cardRepository.read(idcardclient) is not None:
            tranzactie.sumamanopera = tranzactie.sumamanopera - \
                                      tranzactie.sumamanopera / 10.0
        if self.__cardRepository.read(idcardclient) is not None \
                and str(masina.GarantieMasina) == "da":
            tranzactie.sumamapiese = 0
        self.__tranzactieRepository.modifica(tranzactie)
        self.__undoRedoService.addUndoRedoOperation(
            ModifyOperation(
                self.__tranzactieRepository, tranzactie_veche, tranzactie))

    def Sortare(self, list, key, reverse: bool):
        n = len(list)
        if reverse is False:
            for i in range(n):
                for j in range(1, n):
                    if key(list[j - 1]) > key(list[j]):
                        list[j - 1], list[j] = list[j], list[j - 1]
        elif reverse is True:
            for i in range(n):
                for j in range(1, n):
                    if key(list[j - 1]) < key(list[j]):
                        list[j - 1], list[j] = list[j], list[j - 1]
        return list

    def ordoneazaMasinile(self):
        sumamasini = {}
        rezultat = []
        for masina in self.__masinaRepository.read():
            for tranz in self.__tranzactieRepository.read():
                if tranz.idmasina == masina.idEntitate:
                    sumamasini[masina.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            sumamasini[tranzactie.idmasina].append(tranzactie.sumamanopera)

        for idMasina in sumamasini:
            rezultat.append({
                "masinaa": self.__masinaRepository.read(idMasina),
                "sumamanoperaa": sumamasini[idMasina]
            })

        return self.Sortare(rezultat,
                            key=lambda sumamasini: sumamasini["sumamanoperaa"],
                            reverse=True)

    def afisareDinInterval(self, start, end):
        tranzactii = self.__tranzactieRepository.read()
        lista = []
        for tranzactie in tranzactii:
            if tranzactie.sumamanopera >= start \
                    and tranzactie.sumamanopera <= end:
                masina = self.__masinaRepository.read(tranzactie.idmasina)
                card_client = self.__cardRepository.read \
                    (tranzactie.idcardclient)
                lista.append(TranzactieViewModel(tranzactie.idEntitate,
                                                 masina,
                                                 card_client,
                                                 tranzactie.sumapiese,
                                                 tranzactie.sumamanopera,
                                                 tranzactie.datasiora))
        return lista

    def stergeTranzactii(self, start, end):
        tranzactii = self.__tranzactieRepository.read()
        data1 = start.split(' ')
        data2 = end.split(' ')
        inceput = data1[0]
        final = data2[0]
        tranzactiestearsa = []
        for tranzactie in tranzactii:
            data = tranzactie.datasiora.split(' ')
            inceput = data[0]
            if inceput <= tranzactie.datasiora <= final:
                tranzactiestearsa.append(tranzactie)
                self.__tranzactieRepository.sterge(tranzactie.idEntitate)

                self.__undoRedoService.addUndoRedoOperation(
                    DeleteMultiply(self.__tranzactieRepository,
                                   tranzactiestearsa))
        return self.getAll()

    def stergere_masina_cascada(self, idMasina):
        masini_sterse = []
        tranzactii_sterse = []
        for masina in self.__masinaRepository.read():
            if masina.idEntitate == idMasina:
                masini_sterse.append(masina)
                self.__masinaRepository.sterge(masina.idEntitate)
                for tranzactie in self.__tranzactieRepository.read():
                    if tranzactie.idmasina == idMasina:
                        tranzactii_sterse.append(tranzactie)
                        self.__tranzactieRepository. \
                            sterge(tranzactie.idEntitate)
        self.__undoRedoService.addUndoRedoOperation(
            MultiDelete(self.__masinaRepository,
                        self.__tranzactieRepository, masini_sterse,
                        tranzactii_sterse))

    def ordonaDupaReduceri(self):
        reducerePerCard = {}
        rezultat = []
        for card in self.__cardRepository.read():
            for tranz in self.__tranzactieRepository.read():
                if tranz.idcardclient == card.idEntitate:
                    reducerePerCard[card.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            reducerePerCard[tranzactie.idcardclient] \
                .append(tranzactie.sumamanopera)

        for idcardclient in reducerePerCard:
            reduceri = reducerePerCard[idcardclient]
            rezultat.append(
                {
                    "card": self.__cardRepository.read(idcardclient),
                    "valoare": reduce(lambda x, y: x + y, reduceri)
                }
            )

        return sorted(rezultat, key=lambda reducere: reducere["valoare"])

    def ordonareDupaReduceri(self):
        valoareReduceri = {}
        rezultat = []
        for card in self.__cardRepository.read():
            valoareReduceri[card.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            if self.__cardRepository.read(tranzactie.idcardclient) is not None:
                valoareReduceri[tranzactie.idcardclient]. \
                    append(0.1 * tranzactie.sumamanopera)

        for idcard in valoareReduceri:
            reduceri = valoareReduceri[idcard]
            rezultat.append({
                "card_client": self.__cardRepository.read(idcard),
                "valoarereduceri": reduce(lambda x, y: x + y, [reduceri])

            })
        return sorted(rezultat, key=lambda valred: valred["valoarereduceri"],
                      reverse=True)

    def Sterge(self, idsters):
        for tranzactie in self.__tranzactieRepository.read():
            if tranzactie.idEntitate == idsters:
                tranzactie_stearsa = self.__tranzactieRepository.read(
                    tranzactie.idEntitate
                )
                self.__tranzactieRepository.sterge(tranzactie.idEntitate)
                self.__undoRedoService.addUndoRedoOperation(
                    DeleteOperation(self.__tranzactieRepository,
                                    tranzactie_stearsa))
