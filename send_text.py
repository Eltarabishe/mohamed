from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC68e55171e7d50e45f9f7a6774d2c8a81"
# Your Auth Token from twilio.com/console
auth_token  = "9131d3f19837d33e5dd20a45b9dfb85d"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+201550564186", 
    from_="+201003805458",
    body="Hello from Python!")

print (message.sid)
