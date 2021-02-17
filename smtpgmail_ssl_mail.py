import smtplib,ssl
smtpServer = "smtp.gmail.com"
fromAddress = FROM_MAIL
toAddress = TO_MAIL
username = MAIL_USERNAME
password = PASSWORD
smtpPort = 465
message = "Hey There .. this message is sent using python"

try:
    server = smtplib.SMTP_SSL(smtpServer, smtpPort)
    server.login(username, password)
    server.sendmail(fromAddress, toAddress, message)
    print("Mail sent")
except:
    print("Failed to Sent Mail")