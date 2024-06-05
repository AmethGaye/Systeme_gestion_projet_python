from classes.membre import Membre


class Equipe:
    def __init__(self):
        self.membres = []

    def __str__(self):
        """
        retourne la list des membres sous format chaine de cractere
        :return: str
        """
        membre = "\n"
        for m in self.membres:
            membre += f"- {m.nom} ({m.role}) \n"
        return membre

    def ajouter_membre(self, membre: Membre):
        """ ajouter un membre """
        self.membres.append(membre)

    def obtenir_membres(self):
        """ obtenir tous les membres """
        return self.membres
