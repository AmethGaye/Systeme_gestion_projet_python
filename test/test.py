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
        membre = Membre("Mamadou Ba", "Développeur")
        tache = Tache("Analyse des besoins", "test", '2024-06-03', '2024-06-10', membre, "Non démarrée")
        projet = Projet("Soumaya", "test", date_debut.date(), date_fin.date())
        risque = Risque("Retard de livraison", 0.4, "Elevé")
        jalon = Jalon("phase 1", date.date())
        equipe = Equipe()
        email_notif = EmailNotificationStrategy()
        sms_notif = SMSNotificationStrategy()
        push_notif = PushNotificationStrategy()
        notifContext = NotificationContext(email_notif)



if __name__ == '__main__':
    unittest.main()
