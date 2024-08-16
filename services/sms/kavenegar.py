from kavenegar import *
from services.sms.interface import SmsClientInterface
import logging


class KavenegarClient(SmsClientInterface):
    def __init__(self, api_key: str):
        self.api = KavenegarAPI(api_key)

    def send_message(self, receiver: str, message: str):
        """
        Send an SMS message using the Kavenegar API.

        Args:
            receiver (str): The phone number of the message recipient.
            message (str): The content of the SMS message.

        Returns:
            str: The message ID of the sent message.

        Raises:
            APIException: An error occurred with the Kavenegar API.
            HTTPException: An HTTP error occurred while sending the message.
        """
        try:
            params = {'receptor': receiver, 'message': message}
            print(params)
            print("client", self.api.headers)
            response = self.api.sms_send(params)
            print("-------------------------------------------", response.code)
            return response.messageid
        except APIException as e:
            logging.error(e)
            raise
        except HTTPException as e:
            logging.error(e)
            raise

