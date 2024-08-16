from abc import ABC, abstractmethod


class SmsClientInterface(ABC):
    @abstractmethod
    def send_message(self, receiver: str, message: str):
        pass
