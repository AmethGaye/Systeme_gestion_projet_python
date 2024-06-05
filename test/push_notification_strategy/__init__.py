from classes.membre import Membre
from notifications.notification_strategy import NotificationStrategy


class PushNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        print(f"Notification par Push envoyé à {destinataire.nom}: {message}")

