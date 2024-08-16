from services.sms.kavenegar import KavenegarClient
from decouple import config


class SMS:
    def __init__(self, sms_client, receiver, sms_message):
        self.sms_client = sms_client
        self.receiver = receiver
        self.sms_message = sms_message

    def return_client_message(self):
        if self.sms_client == "kavenegar":
            return KavenegarClient(config("SECRET_KEY_KAVENEGAR"))

    # Usage
    # client = KavenegarClient(config('SECRET_KEY_KAVENEGAR'))
    # client.send_message('1234567890', 'Hello, World!')

    def send_message(self):
        client = self.return_client_message()
        return client.send_message(self.receiver, self.sms_message)
