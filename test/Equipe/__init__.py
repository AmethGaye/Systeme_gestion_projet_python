from classes import Membre


class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre: Membre) -> None:
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres
