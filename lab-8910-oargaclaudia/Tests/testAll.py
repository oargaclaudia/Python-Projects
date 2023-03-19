from Tests.testRepositoryInMemory import test_modifica, test_read_adauga
from Tests.testUndoRedo import test_undo


def testAll():
    test_modifica()
    test_read_adauga()
    test_undo()
