import datetime
from classes.Changement import Changement
from classes.Equipe import Equipe
from classes.Jalon import Jalon
from classes.Membre import Membre
from classes.Risque import Risque
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
        self.notifier(f'Nouvelle tache ajoutée: {tache.nom}', self.equipe.obtenir_membres())

    def ajouter_membre_equipe(self, membre: Membre):
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajoutée à l'équipe", self.equipe.obtenir_membres())

    def definir_budget(self, budget: float):
        self.budget = budget
        self.notifier(f"Le budget du projet a été défini à {self.budget} FCFA", self.equipe.obtenir_membres())

    def ajouter_risque(self, risque: Risque):
        self.risques.append(risque)
        self.notifier(f"Nouveau risque ajouté: {risque.description}", self.equipe.obtenir_membres())

    def ajouter_jalon(self, jalon: Jalon):
        self.jalons.append(jalon)
        self.notifier(f"Nouveau jalon ajouté: {jalon.nom}", self.equipe.obtenir_membres())

    def enregistrer_changement(self, description: str):
        self.changements.append(Changement(description, self.version, datetime.time()))
        self.version += 1
        self.notifier(f"Changement enregistré: {description} (version {self.version})", self.equipe.obtenir_membres())

    def calculer_chemin_critique(self):
        # Implémenter la logique de calcul du chemin critique ici
        pass

    def generer_rapport_performance(self):
        # Implémenter la logique de génération de rapport de performance ici
        pass

    def notifier(self, message: str, destinataires):
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)


