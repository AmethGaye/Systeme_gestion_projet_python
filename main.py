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

