import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY
FROM_EMAIL
TO_EMAIL

message = Mail(
    from_email='FROM_EMAIL',
    to_emails='TO_EMAIL',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = SendGridAPIClient(SENDGRID_API_KEY)
response = sg.send(message)
print(response.status_code, response.body, response.headers)        