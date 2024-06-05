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
from unittest.mock import patch
from unittest.mock import MagicMock
from io import StringIO


class TestAll(unittest.TestCase):
    def setUp(self):
        date_debut = datetime(2024, 5, 1)
        date_fin = datetime(2024, 7, 6)
        date = datetime(2024, 6, 3)
        # instance des classes
        self.membre1 = Membre("Mamadou Ba", "Développeur")
        self.membre2 = Membre("Khady Niang", "Testeur")
        self.tache = Tache(
            "Analyse des besoins",
            "test",
            datetime(2024, 6, 3).date(),
            datetime(2024, 7, 12).date(),
            self.membre1,
            "Terminée",
        )
        self.tache1 = Tache(
            "Developpement",
            "phase de devolpppement",
            datetime(2024, 4, 3).date(),
            datetime(2024, 8, 12).date(),
            self.membre1,
            "Non démarrée",
        )
        self.projet = Projet("Soumaya", "test", date_debut.date(), date_fin.date())
        self.risque = Risque("Retard de livraison", 0.4, "Elevé")
        self.jalon = Jalon("phase 1", date.date())
        self.equipe = Equipe()
        self.email_notif = EmailNotificationStrategy()
        self.sms_notif = SMSNotificationStrategy()
        self.push_notif = PushNotificationStrategy()
        self.msg = "Nouvelle tache ajoutée: Analyse des besoins"
        self.notifContext = NotificationContext(self.email_notif)
        self.message = "Nouvelle tache ajoutée: Developpement"
        self.destinataires = [self.membre1, self.membre2]

    """ tester les methodes de la classe Projet """

    def test_ajouter_membre_equipe(self):
        self.projet.ajouter_membre_equipe(self.membre2)
        self.assertIn(self.membre2, self.projet.equipe.membres)

    # methode pour tester la methode definir_budget dans la classe Projet
    def test_definir_budget(self):
        nouveau_budget = 500000.00
        self.projet.definir_budget(nouveau_budget)
        self.assertEqual(self.projet.budget, nouveau_budget)

    # methode pour tester la methode enregistrer_changement dans la classe Projet

    def test_enregistrer_changement(self):
        date_changement = datetime(2024, 3, 12)
        changement = Changement("La duree du projet", 2, date_changement)
        self.projet.changements.append(changement)
        self.assertIn(changement, self.projet.changements)
        self.assertEqual(changement.date, date_changement)

    # Methode pour tester la methode calculer_chemin_critique dans la classe Projet
    def test_calculer_chemin_critique(self):
        self.projet.ajouter_tache(self.tache)
        self.projet.ajouter_tache(self.tache1)
        self.projet.calculer_chemin_critique()

        # Vérification du chemin critique
        chemin_critique_attendu = [self.tache, self.tache1]
        self.assertEqual(self.projet.chemin_critique, chemin_critique_attendu)

    def test_ajouter_tache(self):
        self.projet.ajouter_tache(self.tache)
        self.assertIn(self.tache, self.projet.taches)

    def test_afficher_taches(self):
        self.projet.ajouter_tache(self.tache)
        self.assertEqual(
            self.projet.afficher_taches(),
            "\n- Analyse des besoins, (2024-06-03 à 2024-07-12), Responsable : Mamadou Ba, Statut : Terminée\n",
        )

    def test_ajouter_risque(self):
        self.projet.ajouter_risque(self.risque)
        self.assertIn(self.risque, self.projet.risques)

    def test_afficher_risques(self):
        self.projet.ajouter_risque(self.risque)
        self.assertEqual(
            self.projet.afficher_risques(),
            "\n- Retard de livraison (Probabilité : 0.4, Impact : Elevé)",
        )

    def test_ajouter_jalon(self):
        self.projet.ajouter_jalon(self.jalon)
        self.assertIn(self.jalon, self.projet.jalons)

    def test_afficher_jalon(self):
        self.projet.ajouter_jalon(self.jalon)
        self.assertEqual(
            self.projet.afficher_jalons(), "\n- phase 1 terminée (2024-06-03)\n"
        )

    """ tester les methodes de la classe Equipe """

    def test_obtenir_membres(self):
        self.equipe.ajouter_membre(self.membre1)
        membres = self.equipe.obtenir_membres()
        self.assertIn(self.membre1, membres)

    """ tester les methodes de la classe Tache """

    def test_ajouter_dependance(self):
        self.tache.ajouter_dependance(self.tache)
        self.assertIn(self.tache, self.tache.dependances)

    def test_mettre_a_jour_statut(self):
        nouveau_statut = "En cour"
        self.tache.mettre_a_jour_statut(nouveau_statut)
        self.assertEqual(self.tache.statut, nouveau_statut)

    """ tester les notifications """

    @patch("sys.stdout", new_callable=StringIO)
    def test_email_envoyer(self, mock_stdout):
        self.email_notif.envoyer(self.msg, self.membre1)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            f"Notification par Email envoyé à Mamadou Ba: {self.msg}",
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_sms_envoyer(self, mock_stdout):
        self.sms_notif.envoyer(self.msg, self.membre1)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            f"Notification par SMS envoyé à Mamadou Ba: {self.msg}",
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_push_envoyer(self, mock_stdout):
        self.push_notif.envoyer(self.msg, self.membre1)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            f"Notification par Push envoyé à Mamadou Ba: {self.msg}",
        )

    def test_notifier(self):
        mock_strategy = MagicMock(spec=EmailNotificationStrategy)
        context = NotificationContext(strategy=mock_strategy)
        context.notifier(self.message, self.destinataires)

        # Vérifier que la méthode envoyer a été appelée avec les bons arguments
        expected_calls = [
            unittest.mock.call(self.message, self.membre1),
            unittest.mock.call(self.message, self.membre2),
        ]
        mock_strategy.envoyer.assert_has_calls(expected_calls, any_order=True)

        # Vérifier que la méthode envoyer a été appelée le bon nombre de fois
        self.assertEqual(mock_strategy.envoyer.call_count, 2)


if __name__ == "__main__":
    unittest.main()
