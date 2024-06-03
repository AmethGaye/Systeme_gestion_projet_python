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
        self.tache = Tache("Analyse des besoins", "test", datetime(2024,6,3), datetime(2024,7,12), self.membre, "Non démarrée")
        self.tache1 = Tache("Developpement", "phase de devolpppement", datetime(2024,6,3), datetime(2024,7,12), self.membre, "Non démarrée")
        self.projet = Projet("Soumaya", "test", date_debut.date(), date_fin.date())
        self.risque = Risque("Retard de livraison", 0.4, "Elevé")
        self.jalon = Jalon("phase 1", date.date())
        self.equipe = Equipe()
        self.email_notif = EmailNotificationStrategy()
        self.sms_notif = SMSNotificationStrategy()
        self.push_notif = PushNotificationStrategy()
        self.notifContext = NotificationContext(self.email_notif)

        self.projet.ajouter_tache(self.tache)
        self.projet.ajouter_tache(self.tache1)






      #methode pour tester la methode ajouter_membre_equipe dans la classe projet
    def test_ajouter_membre_equipe(self):
        nouveau_membre = Membre('Khady Niang', 'Testeur')
        self.projet.ajouter_membre_equipe(nouveau_membre)
        self.assertIn(nouveau_membre, self.projet.equipe.membres)

    # methode pour tester la methode definir_budget dans la classe Projet
    def test_definir_budget(self):
        nouveau_budget = 500000.00
        self.projet.definir_budget(nouveau_budget)
        self.assertEqual(self.projet.budget,nouveau_budget)

    #methode pour tester la methode enregistrer_changement dans la classe Projet

    def test_enregistrer_changement(self):
        date_changement = datetime(2024,3,12)
        changement = Changement('La duree du projet',2,date_changement )
        self.projet.changements.append(changement)
        self.assertIn(changement,self.projet
                      .changements)
        self.assertEqual(changement.date,date_changement)


    #Methode pour tester la methode calculer_chemin_critique dans la classe Projet
    def test_calculer_chemin_critique(self):
        self.projet.calculer_chemin_critique()

        # Vérification du chemin critique
        chemin_critique_attendu = [self.tache, self.tache1]
        self.assertEqual(self.projet.chemin_critique, chemin_critique_attendu)



if __name__ == '__main__':
    unittest.main()
