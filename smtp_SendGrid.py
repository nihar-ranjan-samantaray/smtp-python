import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
msg = MIMEMultipart()
message = "This is an email"
 
msg['From'] = "nihar@centroxy.com"
msg['To'] = "nihar@yopmail.com"
msg['Subject'] = "Hello From SendGrid"

apikey= "apikey"
#password="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"
password = os.getenv('SENDGRID_API_KEY')
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.sendgrid.net: 587')
server.starttls()
server.login(apikey, password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
print("mail sent")
server.quit()