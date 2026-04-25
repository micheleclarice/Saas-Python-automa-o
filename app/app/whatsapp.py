from twilio.rest import Client
import os

client = Client(
    os.getenv("TWILIO_SID"),
    os.getenv("TWILIO_TOKEN")
)


def send_whatsapp(to: str, msg: str):
    client.messages.create(
        from_=os.getenv("TWILIO_NUMBER"),
        to=f"whatsapp:{to}",
        body=msg
    )