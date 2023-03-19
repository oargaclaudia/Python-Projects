from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass  # constructorul care genereaza in spate get-uri si set-uri
class Card(Entitate):
    nume: str
    prenume: str
    CNP: str
    datanasterii: str
    datainregistrarii: str
