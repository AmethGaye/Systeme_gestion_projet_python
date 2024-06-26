from datetime import datetime
from classes.projet import Projet
from classes.membre import Membre
from classes.tache import Tache
from classes.jalon import Jalon
from classes.risque import Risque
from notifications.email_notification_strategy import EmailNotificationStrategy


date_debut = datetime(2024, 1, 1)
date_fin = datetime(2024, 12, 31)
membre1 = Membre("Mouhamed", "Chef de projet")
membre2 = Membre("Mamadou", "Développeur")
# stratégie de notification : notification par email
projet1 = Projet("Soumaya", "test", date_debut, date_fin)
projet1.set_notification_strategy(EmailNotificationStrategy())
projet1.definir_budget(350000)
risque1 = Risque("Retard de livraison", 0.4, "Elevé")
dateDebut = datetime(2024, 1, 1)

dateFin = datetime(2024, 1, 31)
dateDebut1 = datetime(2024, 2, 1)
dateFin1 = datetime(2024, 6, 30)
tache1 = Tache("Analyse des besoins", "test",
               dateDebut, dateFin, membre2, "Terminée")
tache2 = Tache("Développement", "test",
               dateDebut1, dateFin1, membre1, "Non démarrée")
tache2.ajouter_dependance(tache1)
date = datetime(2022, 4, 4)
jalon1 = Jalon("phase 1", date)
projet1.ajouter_membre_equipe(membre1)
projet1.ajouter_membre_equipe(membre2)
projet1.ajouter_tache(tache1)
projet1.ajouter_tache(tache2)
projet1.ajouter_jalon(jalon1)
projet1.ajouter_risque(risque1)
projet1.calculer_chemin_critique()
print(projet1)
