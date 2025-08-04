from http.client import HTTPException
import requests
from services.sms.interface import SmsClientInterface

class FarazSmsClient(SmsClientInterface):
    def __init__(self, api_key: str):
        self.header = api_key

    def send_message(self, receiver: str, message: str):
        """
        Send an SMS message using the Kavenegar API.

        Args:
            receiver (str): The phone number of the message recipient.
            message (str): The content of the SMS message.

        Returns:
            ...

        Raises:
            APIException: An error occurred with the Kavenegar API.
            HTTPException: An HTTP error occurred while sending the message.
        """
        print("re", receiver)
        params = {
          "sending_type": "pattern",
          "from_number": "+983000505",
          "code": "lhuw23odggcblm9",
          "recipients": [receiver],
          "params": {
            "verification-code": message
          }
        }
        print(params)
        headers = {
          "Content-Type": "application/json",
          "Authorization": self.header
        }
        response = requests.post(url="https://edge.ippanel.com/v1/api/send", json=params, headers=headers)
        return response


