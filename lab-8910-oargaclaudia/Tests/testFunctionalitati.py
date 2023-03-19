from Domain.card import Card
from Domain.cardValidator import CardValidator
from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repositoryInMemory import RepositoryInMemory
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService


def test_get_all_adauga():
    repository = RepositoryInMemory()
    validare = MasinaValidator()
    undoRedoService = UndoRedoService()
    service_masina = MasinaService(repository, validare, undoRedoService)

    test_masina1 = Masina("1", "bmw", 2009, 123, "nu")
    test_masina2 = Masina("2", "golf", 2021, 100, "da")
    service_masina.adauga("1", "bmw", 2021, 120)
    service_masina.adauga("2", "golf", 2012, 130)

    masini = service_masina.getAll()
    assert len(masini) == 2
    assert masini[0] == test_masina1
    assert masini[1] == test_masina2

    repository_cardClient = RepositoryInMemory()
    validare_cardClient = CardValidator()
    service_cardClient = CardService(repository_cardClient,
                                     validare_cardClient, undoRedoService)

    test_card1 = Card("1", "Ana", "Pop",
                      "1111111111", "12.02.2001",
                      "12.01.2002")
    test_card2 = \
        Card("2", "Claudia", "Oarga",
             "1110000000", "13.07.2002",
             "10.08.2021")
    service_cardClient.adauga("1", "Ana", "Pop",
                              "1111111111", "12.02.2001",
                              "12.01.2002")
    service_cardClient.adauga("2", "Claudia", "Oarga",
                              "1110000000", "13.07.2002",
                              "10.08.2021")

    carduri = service_cardClient.getAll()
    assert len(carduri) == 2
    assert carduri[0] == test_card1
    assert carduri[1] == test_card2


def test_sterge():
    repository_masina = RepositoryInMemory()
    validare_masina = MasinaValidator()
    undoRedoService = UndoRedoService()
    service_masina = MasinaService(repository_masina,
                                   validare_masina,
                                   undoRedoService)

    service_masina.adauga("1", "bmw", 2021, 120)
    service_masina.adauga("2", "golf", 2012, 130)

    masini = service_masina.getAll()
    assert len(masini) == 2

    service_masina.sterge("1")
    masini = service_masina.getAll()
    assert len(masini) == 1

    repository_cardClient = RepositoryInMemory()
    validare_cardClient = CardValidator()
    tranzactieRepository = RepositoryInMemory()
    service_cardClient = \
        CardService(repository_cardClient,
                    validare_cardClient, undoRedoService)

    service_cardClient \
        .adauga("1", "Daniel", "Lupas", 503123123, "14.03.2002", "12.09.2021")
    service_cardClient \
        .adauga("2", "Daniela", "As", 5033213213, "14.05.2002", "12.09.2021")

    carduri = service_cardClient.getAll()
    assert len(carduri) == 2
    service_cardClient.sterge("1")
    service_cardClient.sterge("2")
    carduri = service_cardClient.getAll()
    assert len(carduri) == 0

    repository_tranzactie = RepositoryInMemory()
    validare_tranzactie = TranzactieValidator()
    masinaRepository = RepositoryInMemory()
    cardRepository = RepositoryInMemory()
    service_tranzactie = TranzactieService(repository_tranzactie,
                                           masinaRepository,
                                           cardRepository,
                                           validare_tranzactie,
                                           undoRedoService)

    service_tranzactie.adauga("1", "2", "3", 123, 333, "14.03.2011 12:20")
    service_tranzactie \
        .adauga("2", "3", "4", 1223, 3533, "11.01.2001 12:20")
