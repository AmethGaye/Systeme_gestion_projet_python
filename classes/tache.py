from datetime import datetime
from classes.membre import Membre
from typing import List


class Tache:
    def __init__(self, nom: str, description: str, date_debut: datetime,
                 date_fin: datetime, responsable: Membre, statut: str):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances: List[Tache] = []

    def ajouter_dependance(self, tache: 'Tache'):
        """ ajoute une nouvelle dependance dans le projet """
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str):
        """ mettre a jour de le statut d'une tache """
        self.statut = statut
