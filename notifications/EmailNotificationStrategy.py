from notifications.NotificationStrategy import NotificationStrategy
from classes import Membre


class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        print(f"Email envoyé à {destinataire.nom}: {message}")
