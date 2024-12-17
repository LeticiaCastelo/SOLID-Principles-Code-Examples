from abc import ABC, abstractmethod

class NotificatorInterface(ABC):
    def send_notification(self, message: str):
        pass
