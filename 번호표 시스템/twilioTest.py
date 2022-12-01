from twilio.rest import Client


class TwilioSMS:
    def __init__(self):
        account_sid = 'AC0338ae515fa6d6a24ee96936886c4933'
        auth_token = '6ea739d71bec1d28b3141b4f8d43b3ae'
        self.client = Client(account_sid, auth_token)

    def sendSMS(self,msg):
        message = self.client.messages.create(
            to="+8201057712978",
            from_="+17262272409",
            body=msg)
        print(message.sid)
