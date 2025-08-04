from django.dispatch import receiver

from services.sms.kavenegar import KavenegarClient
from services.sms.farazsms import FarazSmsClient
from decouple import config


class SMS:
    def __init__(self, sms_client, phone, message):
        self.sms_client = sms_client
        self.receiver = phone
        self.sms_message = message

    def return_client_message(self):
        if self.sms_client == "kavenegar":
            return KavenegarClient(config("SECRET_KEY_KAVENEGAR"))
        if self.sms_client == "faraz":
            return FarazSmsClient(config("API_KEY_FRAZA"))

    def send_message(self):
        client = self.return_client_message()
        return client.send_message(receiver=self.sms_message, message=self.receiver)
