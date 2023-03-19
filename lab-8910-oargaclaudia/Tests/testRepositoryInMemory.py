from Domain.masina import Masina
from Repository.repositoryInMemory import RepositoryInMemory


def test_read_adauga():
    repository = RepositoryInMemory()
    masina1 = Masina("1", "opel", 2002, 100, "da")
    masina2 = Masina("2", "bmw", 2003, 400, "nu")
    repository.adauga(masina1)
    repository.adauga(masina2)
    masini = repository.read()
    assert (len(masini)) == 2
    assert masini[0] == masina1
    assert masini[1] == masina2

    assert repository.read("1") == masina1
    assert repository.read("2") == masina2
    assert repository.read("5") is None


def test_delete():
    repository = RepositoryInMemory()
    masina1 = Masina("1", "opel", 2002, 100, "da")
    masina2 = Masina("2", "bmw", 2003, 400, "nu")
    repository.adauga(masina1)
    repository.adauga(masina2)
    repository.sterge("1")
    assert repository.read("1") is None
    assert repository.read("2") is not None

    repository.sterge("2")
    assert repository.read("1") is None
    assert repository.read("2") is None


def test_modifica():
    repository = RepositoryInMemory()
    masina1 = Masina("1", "opel", 2002, 100, "da")
    masina2 = Masina("2", "bmw", 2003, 400, "nu")
    repository.adauga(masina1)
    repository.adauga(masina2)
    masina1_noua = Masina("1", "bmw", 2003, 200, "nu")
    masina2_noua = Masina("2", "opel", 2004, 100, "da")
    repository.modifica(masina1_noua)
    repository.modifica(masina2_noua)

    assert repository.read("1") == masina1_noua
    assert repository.read("2") == masina2_noua
