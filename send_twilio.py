from twilio.rest import Client 

TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN
FROM_NUMBER
TO_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) 
  
message = client.messages.create( 
                              from_='FROM_NUMBER', 
                              body ='Twilio Test', 
                              to ='TO_NUMBER'
                          ) 
  
print(message.sid) 