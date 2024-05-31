from classes import Membre
from notifications.NotificationStrategy import NotificationStrategy


class PushNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        print(f"Push notification envoyé à {destinataire.nom}: {message}")

