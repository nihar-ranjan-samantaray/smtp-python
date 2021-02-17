import smtplib,ssl
smtpServer = "mail.smtp2go.com"
fromAddress = FROM_MAIL
toAddress = TO_MAIL
username = MAIL_USERNAME
password = PASSWORD
smtpPort = 25
message = "Hey There .. this message is sent using python"

try:
    server = smtplib.SMTP(smtpServer, smtpPort)
    server.login(username, password)
    server.sendmail(fromAddress, toAddress, message)
    print("Mail sent")
except Exception as e:
    print("Failed to Sent Mail : ",e)