from classes.membre import Membre
from notifications.notification_strategy import NotificationStrategy


class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def notifier(self, message: str, destinataires: Membre):
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)
