from classes import Membre
from notifications.NotificationStrategy import NotificationStrategy


class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        print(f"SMS envoyé à {destinataire.nom}: {message}")
