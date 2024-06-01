<<<<<<< HEAD
from datetime import datetime
from classes.Projet import Projet
from classes.Membre import Membre
from classes.Tache import Tache
from classes.Jalon import Jalon
from classes.Risque import Risque

date_debut = datetime(2022,3,4)
date_fin = datetime(2023,3,5)
membre1 = Membre("Mouhamed","Chef de projet")
membre2 = Membre("Mamadou","Développeur")
projet1 = Projet("Soumaya", "test", date_debut.date(), date_fin.date())
projet1.definir_budget(350000)
risque1 = Risque("Retard de livraison", 0.4 ,"Elevé")
dateDebut = datetime(2022, 4, 6)
dateFin = datetime(2022 , 7, 6)
tache1 = Tache("Analyse des besoins","test",dateDebut.date(), dateFin.date(), membre2,"Non démarrée")
tache2 = Tache("Développement","test",dateDebut.date(), dateFin.date(), membre1,"Terminée")
date = datetime(2022, 4, 4)
jalon1 = Jalon("phase 1", date.date())
projet1.ajouter_membre_equipe(membre1)
projet1.ajouter_membre_equipe(membre2)
projet1.ajouter_tache(tache1)
projet1.ajouter_tache(tache2)
projet1.ajouter_jalon(jalon1)
projet1.ajouter_risque(risque1)

print(projet1)
=======
from classes.Jalon import Jalon
from classes.Membre import Membre
from classes.Projet import Projet
from classes.Risque import Risque
from classes.Tache import Tache
from notifications.EmailNotificationStrategy import EmailNotificationStrategy


if __name__ == '__main__':
    projet = Projet('projet A', 'this is my first project', '2024-05-31', '2024-06-15')

    # stratégie de notification : notification par email
    projet.set_notification_strategy(EmailNotificationStrategy())

    # ajouter les membres de l'equipe
    # projet.ajouter_membre_equipe(Membre('Mouhamad Gaye', 'Developpeur front-end'))
    projet.ajouter_membre_equipe(Membre('Khady Niang', 'Architect logiciel'))
    projet.ajouter_membre_equipe(Membre('Mamadou Ba', 'Developpeur back-end'))

    # ajouter une nouvelle tache
    projet.ajouter_tache(Tache('Developpement', 'Description du tache nouvellement ajoutée',
                               '2024-06-01', '2024-06-05',
                               projet.equipe.obtenir_membres()[0], 'en cours'))

    # ajouter un nouveau risque
    projet.ajouter_risque(Risque('Retard de livraison', 0.2, 'Elevé'))

    # ajouter un nouveau jalon
    projet.ajouter_jalon(Jalon('Phase 1 terminée', '2024-06-01'))

    # enregistrer un changement
    projet.enregistrer_changement('Changement de la portée du projet')

>>>>>>> ff824910a34c5e59a5c6a3e82c3ec2e4835a87c7
