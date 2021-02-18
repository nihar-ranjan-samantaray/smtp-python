import os
import requests
from random import randint

MAILGUN_API_KEY = 
MAILGUN_DOMAIN = 
FROM_TITLE = 
FROM_EMAIL = 
TO_EMAIL = 

randotp = randint(000000,999999)
request = requests.post(f"https://api.mailgun.net/v2/{MAILGUN_DOMAIN}/messages",
            auth=("api" , MAILGUN_API_KEY),
            data={
            "from": f"{FROM_TITLE} <{FROM_EMAIL}> ",
            "to": TO_EMAIL ,
            "subject": "OTP code for UTG Registration",
            "text": f"Please note down the 6 digit code - {randotp}. Please go back to the mobile app and enter to continue with account registration" ,
        },)

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))
