import smtplib 
smtpServer = "smtp.gmail.com"
fromAddress = FROM_MAIL
toAddress = TO_MAIL
username = MAIL_USERNAME
password = PASSWORD
smtpPort = 587
message = "Hey There .. this message is sent using python"
  
try:
    server = smtplib.SMTP(smtpServer, smtpPort) 
    server.starttls() 
    server.login(username, password) 
    server.sendmail(fromAddress, toAddress, message) 
    print("Mail Sent")
    server.quit()
except:
    print("Failed to Sent Mail")