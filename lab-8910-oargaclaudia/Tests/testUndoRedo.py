from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Repository.repositoryInMemory import RepositoryInMemory
from Service.masinaService import MasinaService
from Service.undoRedoService import UndoRedoService


def test_undo():
    masinaRepository = RepositoryInMemory()
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository,
                                  masinaValidator,
                                  undoRedoService)
    masina1 = Masina('1', 'bentley', 2010, 10, 'da')
    masina2 = Masina('2', 'audi', 2020, 2020, 'da')
    masina3 = Masina('3', 'mercedes', 2012, 2015, 'nu')

    masinaService.adauga('1', 'bentley', 2010, 10)
    undoRedoService.undo()

    assert len(masinaRepository.read()) == 0

    masinaService.adauga('2', 'audi', 2020, 2020)
    masinaService.adauga('3', 'mercedes', 2012, 2015)
    undoRedoService.undo()

    assert masinaRepository.read() == [masina2]

    undoRedoService.undo()
    assert masinaRepository.read() == []
