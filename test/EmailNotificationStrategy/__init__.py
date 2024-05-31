from classes import Membre
from notifications.NotificationStrategy import NotificationStrategy


class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: 'Membre'):
        print(f"Email envoyé à {destinataire.nom}: {message}")
