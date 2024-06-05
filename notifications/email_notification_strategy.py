from notifications.notification_strategy import NotificationStrategy
from classes.membre import Membre as Membre


class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: 'Membre'):
        print(f"Notification par Email envoyé à {destinataire.nom}: {message}")
