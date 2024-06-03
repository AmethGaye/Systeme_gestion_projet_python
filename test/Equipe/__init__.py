from classes.Membre import Membre


class Equipe:
    def __init__(self):
        self.membres = []

    def __str__(self):
        membre = "\n"
        for m in self.membres:
            membre += f"- {m.nom} ({m.role}) \n";
        return membre

    def ajouter_membre(self, membre: Membre):
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres