import unittest
from datetime import datetime
from classes.Changement import Changement
from classes.Equipe import Equipe
from classes.Jalon import Jalon
from classes.Membre import Membre
from classes.Projet import Projet
from classes.Risque import Risque
from classes.Tache import Tache
from notifications.EmailNotificationStrategy import EmailNotificationStrategy
from notifications.NotificationContext import NotificationContext
from notifications.PushNotificationStrategy import PushNotificationStrategy
from notifications.SMSNotificationStrategy import SMSNotificationStrategy


class TestProjet(unittest.TestCase):
    def setUp(self):
        date_debut = datetime(2024, 5, 1)
        date_fin = datetime(2024, 7, 6)
        date = datetime(2024, 6, 3)
        # instance des classes
        self.membre = Membre("Mamadou Ba", "Développeur")
        self.tache = Tache("Analyse des besoins", "test", '2024-06-03', '2024-06-10', self.membre, "Non démarrée")
        self.projet = Projet("Soumaya", "test", date_debut.date(), date_fin.date())
        self.risque = Risque("Retard de livraison", 0.4, "Elevé")
        self.jalon = Jalon("phase 1", date.date())
        self.equipe = Equipe()
        self.email_notif = EmailNotificationStrategy()
        self.sms_notif = SMSNotificationStrategy()
        self.push_notif = PushNotificationStrategy()
        self.notifContext = NotificationContext(self.email_notif)




installed_packages = [pkg.key for pkg in pkg_resources.working_set]
print(installed_packages)

if __name__ == '__main__':
    unittest.main()
