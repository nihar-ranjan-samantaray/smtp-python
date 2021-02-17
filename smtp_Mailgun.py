import os
import requests
from random import randint

MAILGUN_API_KEY = 'ec674077e581b54c8b7821b4b02f01ea-4de08e90-c43d8c37'
MAILGUN_DOMAIN = 'sandboxd09cf6814c6e4186a780fd232d72bb67.mailgun.org'
FROM_TITLE = 'U TURN GREEN'
FROM_EMAIL = 'nihar@centroxy.com'
TO_EMAIL = 'nihar@yopmail.com'

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