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

    def __init__(self, nom: str, description: str, date_debut: datetime.datetime, date_fin: datetime.datetime):
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

    def __str__(self):
        return f"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" \
               f"\nRapport d'activités du projet '{self.nom}' :\nVersion : {self.version}\nDates : {self.date_debut} à {self.date_fin}\nBudget : {self.budget} FCFA\nEquipe :" \
               f" {self.equipe}Tâche : {self.afficher_taches()}Jalons : {self.afficher_jalons()}Risques : " \
               f"{self.afficher_risques()}\nChemin Critique : {self.afficher_chemin_critique()}"

    def set_notification_strategy(self, strategy: NotificationStrategy):
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache):
        self.taches.append(tache)
        self.notifier(f'Nouvelle tache ajoutée: {tache.nom}', self.equipe.obtenir_membres())

    def afficher_taches(self):
        tache = "\n"
        for val in self.taches:
            tache += f"- {val.nom}, ({val.date_debut} à {val.date_fin}), Responsable : {val.responsable.nom}, Statut : {val.statut}\n"
        return tache

    def ajouter_membre_equipe(self, membre: Membre):
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajoutée à l'équipe", self.equipe.obtenir_membres())

    def definir_budget(self, budget: float):
        self.budget = budget
        self.notifier(f"Le budget du projet a été défini à {self.budget} FCFA", self.equipe.obtenir_membres())

    def ajouter_risque(self, risque: Risque):
        self.risques.append(risque)
        self.notifier(f"Nouveau risque ajouté: {risque.description}", self.equipe.obtenir_membres())

    def afficher_risques(self):
        risque = "\n"
        for val in self.risques:
            risque += f"- {val.description} (Probabilité : {val.probabilite}, Impact : {val.impact})"
        return risque

    def ajouter_jalon(self, jalon: Jalon):
        self.jalons.append(jalon)
        self.notifier(f"Nouveau jalon ajouté: {jalon.nom}", self.equipe.obtenir_membres())

    def afficher_jalons(self):
        jalon = "\n"
        for val in self.jalons:
            jalon += f"- {val.nom} terminée ({val.date})\n"
        return jalon

    def enregistrer_changement(self, description: str):
        self.changements.append(Changement(description, self.version, datetime.datetime.now()))
        self.version += 1
        self.notifier(f"Changement enregistré: {description} (version {self.version})", self.equipe.obtenir_membres())

    def calculer_chemin_critique(self):
        date_debut_tot = {tache: tache.date_debut for tache in self.taches}
        date_fin_tot = {tache: tache.date_fin for tache in self.taches}
        date_debut_tard = {}
        date_fin_tard = {}

        # Calcul des dates au plus tôt
        for tache in self.taches:
            if tache.dependances:
                date_debut_tot[tache] = max(date_fin_tot[dependance] for dependance in tache.dependances)
            date_fin_tot[tache] = date_debut_tot[tache] + (tache.date_fin - tache.date_debut)

        # Tâche finale pour commencer la propagation des dates au plus tard
        tache_finale = max(self.taches, key=lambda t: date_fin_tot[t])
        date_fin_tard[tache_finale] = date_fin_tot[tache_finale]
        date_debut_tard[tache_finale] = date_fin_tard[tache_finale] - (tache_finale.date_fin - tache_finale.date_debut)

        # Initialisation des dates de début et fin au plus tard pour les autres tâches
        for tache in self.taches:
            if tache != tache_finale:
                date_fin_tard[tache] = datetime.datetime.max
                date_debut_tard[tache] = datetime.datetime.max

        # Calcul des dates au plus tard
        for tache in reversed(self.taches):
            if tache != tache_finale and tache.dependances:
                date_fin_tard[tache] = min(date_debut_tard[dependance] for dependance in tache.dependances)
            date_debut_tard[tache] = date_fin_tard[tache] - (tache.date_fin - tache.date_debut)

        # Identification des tâches du chemin critique
        self.chemin_critique = [tache for tache in self.taches ]

    def afficher_chemin_critique(self):
        tache = "\n"
        for val in self.chemin_critique:
            tache += f"- {val.nom} ({val.date_debut} à {val.date_fin})\n"
        return tache

    def notifier(self, message: str, destinataires):
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)
