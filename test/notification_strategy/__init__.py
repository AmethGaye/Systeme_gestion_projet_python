from classes.membre import Membre
from abc import ABC, abstractmethod


class NotificationStrategy(ABC):

    @abstractmethod
    def envoyer(self, message: str, destinataire: Membre):
        pass

