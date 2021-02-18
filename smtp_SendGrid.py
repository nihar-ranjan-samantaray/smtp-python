import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
msg = MIMEMultipart()
message = "This is an email"
 
FROM_MAIL
TO_MAIL
SENDGRID_API_KEY

msg['From'] = FROM_MAIL
msg['To'] = TO_MAIL
msg['Subject'] = "Hello From SendGrid"

apikey= "apikey"

password = SENDGRID_API_KEY
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.sendgrid.net: 587')
server.starttls()
server.login(apikey, password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
print("mail sent")
server.quit()
