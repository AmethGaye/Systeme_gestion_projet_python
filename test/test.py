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


class TestEquipe(unittest.TestCase):
    def setUp(self):
        self.equipe = Equipe()
        self.membre1 = Membre("khady", "développeur")

    def test_ajouter_membre(self):
        self.equipe.ajouter_membre(self.membre1)
        self.assertIn(self.membre1, self.equipe.obtenir_membres())

    def test_obtenir_membres(self):
        self.equipe.ajouter_membre(self.membre1)
        membres = self.equipe.obtenir_membres()
        self.assertIn(self.membre1, membres)


class TestTache(unittest.TestCase):
    def setUp(self):
        self.membre = Membre("Mamadou Ba", "Développeur")
        self.tache = Tache("Analyse des besoins", "test", '2024-06-03', '2024-06-10', self.membre, "Terminée")

    def test_ajouter_dependance(self):
        self.tache.ajouter_dependance(self.tache)
        self.assertIn(self.tache, self.tache.dependances)

    def test_mettre_a_jour_statut(self):
        nouveau_statut = "En cour"
        self.tache.mettre_a_jour_statut(nouveau_statut)
        self.assertEqual(self.tache.statut, nouveau_statut)


class TestProjet(unittest.TestCase):
    def setUp(self):
        date_debut = datetime(2024, 5, 1)
        date_fin = datetime(2024, 7, 6)
        date = datetime(2024, 6, 3)
        # instance des classes
        membre = Membre("Mamadou Ba", "Développeur")
        self.tache = Tache("Analyse des besoins", "test", '2024-06-03', '2024-06-10', membre, "Terminée")
        self.projet = Projet("Soumaya", "test", date_debut, date_fin)
        self.risque = Risque("Retard de livraison", 0.4, "Elevé")
        self.jalon = Jalon("phase 1", date.date())
        equipe = Equipe()
        email_notif = EmailNotificationStrategy()
        sms_notif = SMSNotificationStrategy()
        push_notif = PushNotificationStrategy()
        notifContext = NotificationContext(email_notif)



    def test_ajouter_tache(self):
        self.projet.ajouter_tache(self.tache)
        self.assertIn(self.tache, self.projet.taches)

    def test_afficher_taches(self):
        self.projet.ajouter_tache(self.tache)
        self.assertEqual(self.projet.afficher_taches(),"\n- Analyse des besoins, (2024-06-03 à 2024-06-10), Responsable : Mamadou Ba, Statut : Terminée\n")

    def test_ajouter_risque(self):
        self.projet.ajouter_risque(self.risque)
        self.assertIn(self.risque, self.projet.risques)

    def test_afficher_risques(self):
        self.projet.ajouter_risque(self.risque)
        self.assertEqual(self.projet.afficher_risques(), "\n- Retard de livraison (Probabilité : 0.4, Impact : Elevé)")

    def test_ajouter_jalon(self):
        self.projet.ajouter_jalon(self.jalon)
        self.assertIn(self.jalon, self.projet.jalons)

    def test_afficher_jalon(self):
        self.projet.ajouter_jalon(self.jalon)
        self.assertEqual(self.projet.afficher_jalons(), "\n- phase 1 terminée (2024-06-03)\n")




if __name__ == '__main__':
    unittest.main()
