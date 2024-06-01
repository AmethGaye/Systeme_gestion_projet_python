from classes import Membre
from notifications.NotificationStrategy import NotificationStrategy


class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def notifier(self, message: str, destinataires):
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)
