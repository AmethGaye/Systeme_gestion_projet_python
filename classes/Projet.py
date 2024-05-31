import datetime

from classes import Membre, Risque, Jalon
from classes.Changement import Changement
from classes.Equipe import Equipe
from classes.Tache import Tache
from notifications.NotificationContext import NotificationContext
from notifications.NotificationStrategy import NotificationStrategy


class Projet:
    def __init__(self, nom: str, description: str, date_debut: datetime, date_fin: datetime):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques = []
        self.jalons = []
        self.version = 1
        self.changements = []
        self.chemin_critique = []
        self.notification_context = None

    def set_notification_strategy(self, strategy: NotificationStrategy):
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache):
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre: Membre):
        self.equipe.ajouter_membre(membre)

    def definir_budget(self, budget: float):
        self.budget = budget

    def ajouter_risque(self, risque: Risque):
        self.risques.append(risque)

    def ajouter_jalon(self, jalon: Jalon):
        self.jalons.append(jalon)

    def enregistrer_changement(self, description: str):
        self.changements.append(Changement(description, self.version, datetime.now()))
        self.version += 1

    def calculer_chemin_critique(self):
        # Implémenter la logique de calcul du chemin critique ici
        pass

    def generer_rapport_performance(self):
        # Implémenter la logique de génération de rapport de performance ici
        pass

    def notifier(self, message: str, destinataires):
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)
