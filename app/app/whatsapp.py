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
    )from twilio.rest import Client

account_sid = ''
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+557592195441'
)

print(message.sid)201 - CREATED - The request was successful. We created a new resource and the response body contains the representation.
{
  "account_sid": "",
  "api_version": "2010-04-01",
  "body": "Your appointment is coming up on 12/1 at 3pm",
  "date_created": "Sat, 25 Apr 2026 15:56:18 +0000",
  "date_sent": null,
  "date_updated": "Sat, 25 Apr 2026 15:56:18 +0000",
  "direction": "outbound-api",
  "error_code": null,
  "error_message": null,
  "from": "whatsapp:+14155238886",
  "messaging_service_sid": null,
  "num_media": "0",
  "num_segments": "1",
  "price": null,
  "price_unit": null,
  "sid": "MMcf98adc24ffafbdd6cf3998a0d0dc365",
  "status": "queued",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/""/Media.json"
  },
  "to": "whatsapp:+557592195441",
  "uri": "/2010-04-01/Accounts/"".json"
}