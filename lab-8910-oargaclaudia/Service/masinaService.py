import datetime

from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.masinaValidator import MasinaValidator
from Domain.masina import Masina
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class MasinaService:
    def __init__(self, masinaRepository: Repository,
                 masinaValidator: MasinaValidator,
                 undoRedoService: UndoRedoService):
        # declar campurile de tip private
        # pentru ca nu am de ce sa
        # le accesez din exterior
        self.__undoRedoService = undoRedoService
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator

    # delegam responsabilitatea spre repository
    # apelam fara niciun parametru pentru ca vrem getAll
    def getAll(self):
        return self.__masinaRepository.read()

    # primesc toti parametrii de la masina
    # pentru ca urmeaza sa ii citesc din userinterface
    def adauga(self, idMasina, modelMasina, anAchizitie, nrKmMasina):
        # ne cream un obiect de tipul Masina
        help_tool =  lambda x: self.__masinaRepository.adauga(x)
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        if nrKmMasina < 60000 and int(year) - int(anAchizitie) <= 3:
            garantieMasina = "da"
        else:
            garantieMasina = "nu"
        masina = Masina(idMasina, modelMasina,
                        anAchizitie, nrKmMasina,
                        garantieMasina)
        # validez masina data
        self.__masinaValidator.valideaza(masina)
        help_tool(masina)
        self.__undoRedoService.addUndoRedoOperation(
            AddOperation(self.__masinaRepository, masina))

    def sterge(self, idMasina):
        help_tool = lambda x: self.__masinaRepository.sterge(x)
        masina_stearsa = self.__masinaRepository.read(idMasina)
        help_tool(idMasina)
        self.__undoRedoService.addUndoRedoOperation(
            DeleteOperation(self.__masinaRepository, masina_stearsa))

    def modifica(self, idMasina, modelMasina, anAchizitie, nrKmMasina):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        masina_veche = self.__masinaRepository.read(idMasina)
        if nrKmMasina < 60000 and int(year) - int(anAchizitie) <= 3:
            garantieMasina = "da"
        else:
            garantieMasina = "nu"
        masina = Masina(idMasina, modelMasina,
                        anAchizitie,
                        nrKmMasina,
                        garantieMasina)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.modifica(masina)
        self.__undoRedoService.addUndoRedoOperation(
            ModifyOperation(self.__masinaRepository, masina_veche, masina))

    def cautareMasina(self, cuvant):
        rezultat = self.__masinaRepository.read()
        return list(filter(lambda x: cuvant in x.modelMasina or
                           cuvant in x.GarantieMasina or
                           cuvant in str(x.nrKmMasina)
                           or cuvant in str(x.anAchizitie),
                           rezultat))
