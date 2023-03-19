from Domain.cardValidator import CardValidator
from Domain.masinaValidator import MasinaValidator
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService
from Tests.testAll import testAll
from UI.consola import Consola


def main():
    undoRedoService = UndoRedoService()
    masinaRepositoryJson = RepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson,
                                  masinaValidator,
                                  undoRedoService)

    cardRepositoryJson = RepositoryJson("carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepositoryJson,
                              cardValidator,
                              undoRedoService)

    tranzactieRepositoryJson = RepositoryJson("tranzactii.json")
    tranzactieValidator = TranzactieValidator()
    tranzactieService = TranzactieService(tranzactieRepositoryJson,
                                          masinaRepositoryJson,
                                          cardRepositoryJson,
                                          tranzactieValidator, undoRedoService)

    consola = Consola(masinaService, cardService,
                      tranzactieService, undoRedoService)

    testAll()
    consola.runMenu()


main()
