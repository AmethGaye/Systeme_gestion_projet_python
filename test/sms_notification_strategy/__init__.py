from classes.membre import Membre
from notifications.notification_strategy import NotificationStrategy


class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        print(f"Notification par SMS envoyé à {destinataire.nom}: {message}")
