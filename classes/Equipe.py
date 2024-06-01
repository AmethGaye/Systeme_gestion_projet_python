from classes.Membre import Membre


class Equipe:
    def __init__(self):
        self.membres = []
<<<<<<< HEAD
    def __str__(self):
        membre = "\n"
        for m in self.membres:
            membre += f"- {m.nom} ({m.role}) \n";
        return membre
    def ajouter_membre(self, membre: Membre) -> None:
=======

    def ajouter_membre(self, membre: Membre):
>>>>>>> ff824910a34c5e59a5c6a3e82c3ec2e4835a87c7
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres
