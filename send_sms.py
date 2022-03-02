# fonte https://www.twilio.com/docs/libraries/python
# pip install twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC105413a5515b9bca0565ef5eb7178b6c"
# Your Auth Token from twilio.com/console
auth_token  = "c4309501eb251238a5a9dd6ee9d0f29a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5548996773435", 
    from_="+13237680831",
    body="teste de envio SMS com Python!. By geanclm in 29/08/2021")
print(message.sid)