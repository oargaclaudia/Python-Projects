import datetime
import random

from Service.masinaService import MasinaService
from Service.cardService import CardService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService


class Consola:
    def __init__(self, masinaService: MasinaService, cardService: CardService,
                 tranzactieService: TranzactieService,
                 undoRedoService: UndoRedoService):

        self.__tranzactieService = tranzactieService
        self.__masinaService = masinaService
        self.__cardService = cardService
        self.__undoRedoService = undoRedoService

    def runMenu(self):
        if True:
            print("1. CRUD masina ")
            print("2. CRUD card client")
            print("3. CRUD tranzactie")
            print("4. Căutare mașini și clienți. Căutare full text.")
            print("5. Genereaza random n masini")
            print("6. Afișarea tuturor tranzacțiilor"
                  " cu suma cuprinsă într-un "
                  "interval dat")
            print("7. Afișarea mașinilor ordonate"
                  " descrescător după suma "
                  "obținută pe manoperă.")
            print("8. Afișarea cardurilor ordonate"
                  "descrescător după valoarea "
                  "reducerilor obținute.")
            print("9. Ștergerea tuturor tranzacțiilor"
                  " dintr-un anumit interval de zile.")
            print("10. Delete in cascada. ")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire din aplicatie")
            optiune = input("Dati optiunea de la tastatura: ")
            if optiune == "1":
                self.runCRUDMasiniMenu()
            elif optiune == "2":
                self.runCRUDCardClientMenu()
            elif optiune == "3":
                self.runCRUDTranzactieMenu()
            elif optiune == "4":
                self.runCautareMenu()
            elif optiune == "5":
                self.runGenerareRandom()
            elif optiune == "6":
                self.runAfisareTranzactiiCuSumaCuprinsaInInterval()
            elif optiune == "7":
                self.uiOrdonareDupaSumaManopera()
            elif optiune == "8":
                self.uiOrdonareDupaReduceri()
            elif optiune == "9":
                self.uiStergeTranzactiiDinInterval()
            elif optiune == "10":
                self.uiStergereInCascada()
            elif optiune == "u":
                self.__undoRedoService.undo()
            elif optiune == "r":
                self.__undoRedoService.redo()

            elif optiune == "x":
                return None
            else:
                print("Optiune invalida! Reincercati! ")
            self.runMenu()

    def runCRUDMasiniMenu(self):
        while True:
            print("1. Adauga masina")
            print("2. Sterge masina")
            print("3. Modifica masina")
            print("a. Afiseaza toate masinile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaMasina()
            elif optiune == "2":
                self.uiStergeMasina()
            elif optiune == "3":
                self.uiModificaMasina()
            elif optiune == "a":
                self.showAllMasini()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincercati! ")

    def runCRUDCardClientMenu(self):
        while True:
            print("1. Adauga card client")
            print("2. Sterge card client")
            print("3. Modifica card client")
            print("a. Afiseaza toate cardurile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaCard()
            elif optiune == "2":
                self.uiStergeCard()
            elif optiune == "3":
                self.uiModificaCard()
            elif optiune == "a":
                self.uishowAllCarduri()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida! Reincercati")

    def runCRUDTranzactieMenu(self):
        while True:
            print("1. Adauga o tranzactie")
            print("2. Sterge o tranzactie")
            print("3. Modifica o tranzactie")
            print("a. Afiseaza toate tranzactiile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaTranzactie()
            elif optiune == "2":
                self.uiStergeTranzactie()
            elif optiune == "3":
                self.uiModificaTranzactie()
            elif optiune == "a":
                self.showAllTranzactii()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida ")

    def uiAdaugaMasina(self):
        # punem intr-un try pentru ca poate sa dea
        # eroare altfel. dupa care prindem exceptiile
        try:
            idMasina = input("Dati id-ul masinii: ")
            modelMasina = input("Dati modelul masinii: ")
            anAchizitie = int(input("Dati anul achiziei masinii: "))
            nrKmMasina = float(input("Dati numarul de km ai masinii: "))

            self.__masinaService.adauga(idMasina, modelMasina,
                                        anAchizitie, nrKmMasina)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de sters: ")
            self.__masinaService.sterge(idMasina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de modificat: ")
            modelMasina = input("Dati noul model al masinii: ")
            anAchizitie = int(input("Dati noul an al achiziei masinii: "))
            nrKmMasina = float(input("Dati noul numar de km ai masinii: "))

            self.__masinaService.modifica(idMasina, modelMasina,
                                          anAchizitie, nrKmMasina)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllMasini(self):
        for masina in self.__masinaService.getAll():
            print(masina)

    def uiAdaugaCard(self):
        try:
            idcard = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            datanasterii = input("Dati data nasterii clientului: ")
            datainregistrarii = input("Dati data inregistrarii: ")

            self.__cardService.adauga(idcard, nume, prenume,
                                      CNP, datanasterii,
                                      datainregistrarii)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeCard(self):
        try:
            idcard = input("Dati id-ul cardului de sters: ")
            self.__cardService.sterge(idcard)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaCard(self):
        try:
            idcard = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            datanasterii = input("Dati data nasterii clientului: ")
            datainregistrarii = input("Dati data inregistrarii: ")

            self.__cardService.modifica(idcard, nume,
                                        prenume, CNP,
                                        datanasterii, datainregistrarii)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uishowAllCarduri(self):
        for card in self.__cardService.getAll():
            print(card)

    def uiAdaugaTranzactie(self):
        try:
            idtranzactie = input("Dati id-ul tranzactiei: ")
            idmasina = input("Dati id-ul masinii: ")
            idcardclient = input("Dati id-ul cardului clientului: ")
            sumapiese = float(input("Dati suma pieselor: "))
            sumamanopera = float(input("Dati suma manoperei: "))
            datasiora = input("Dati  data si  ora: ")

            self.__tranzactieService.adauga(idtranzactie, idmasina,
                                            idcardclient,
                                            sumapiese, sumamanopera,
                                            datasiora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeTranzactie(self):
        try:
            id = input("Dati id-ul tranzactiei de sters: ")
            self.__tranzactieService.sterge(id)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaTranzactie(self):
        try:
            idtranzactie = input("Dati id-ul tranzactiei de modificat: ")
            idmasina = input("Dati noul id al masinii: ")
            idcardclient = input("Dati noul card al clientului: ")
            sumapiese = float(input("Dati noua suma pieselor: "))
            sumamanopera = float(input("Dati noua suma a manoperei: "))
            datasiora = input("Dati noua data si noua ora: ")

            self.__tranzactieService.modifica(idtranzactie, idmasina,
                                              idcardclient, sumapiese,
                                              sumamanopera, datasiora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllTranzactii(self):
        for tranzactie in self.__tranzactieService.getAll():
            print(tranzactie)

    def runCautareMenu(self):
        cuvant = input("Dati cuvantul dupa care se cauta textul: ")
        cautare1 = self.__cardService.cautareCardClient(cuvant)
        cautare2 = self.__masinaService.cautareMasina(cuvant)
        print(cautare1)
        print(cautare2)

    def runGenerareRandom(self):
        idMasina = 0
        n = int(input("Dati numarul de masini pe care vreti sa il generati: "))
        numemasini = ["opel", "logan", "dacia"]
        listagarantie = ["da", "nu"]
        for i in range(n):
            try:
                idMasina = random.randint(1, 200)
                modelMasina = random.choice(numemasini)
                GarantieMasina = random.choice(listagarantie)
                anAchizitie = random.randint(1990, 2021)
                nrKmMasina = random.randint(100, 3000)
                self.__masinaService.adauga(idMasina,
                                            modelMasina,
                                            anAchizitie,
                                            nrKmMasina)
                idMasina = idMasina + 1
                print("Masina adaugata cu succes!")
            except Exception as e:
                print(e)

    def uiOrdonareDupaSumaManopera(self):
        try:
            for masini in self.__tranzactieService.ordoneazaMasinile():
                print(masini)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def runAfisareTranzactiiCuSumaCuprinsaInInterval(self):
        try:
            start = float(input("Dati numarul de la care incepe intervalul: "))
            final = float(input("Dati numarul la care se termina intervalul:"))
            y = self.__tranzactieService.afisareDinInterval(start, final)
            for tranzactie in y:
                print(tranzactie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeTranzactiiDinInterval(self):
        start = input("Dati ziua si ora de la care incepe intervalul:")
        end = input("Dati ziua si ora in care se termina intervalul:")
        self.__tranzactieService.stergeTranzactii(start, end)

    def uiOrdonareDupaReduceri(self):
        for card in self.__tranzactieService.ordonareDupaReduceri():
            print(card)

    def uiStergereInCascada(self):
        try:
            idSters = input("Introdu id-ul pentru"
                            " a incepe stergerea in cascada: ")
            self.__tranzactieService.stergere_masina_cascada(idSters)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
