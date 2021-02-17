from flask import *  
from flask_mail import *
import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from random import randint  
app = Flask(__name__)  
 
mail = Mail(app)  
otp = randint(000000,999999) 
  
SENDGRID_API_KEY
SENDGRID_MAIL_FROM
@app.route('/')  
def index():
    return render_template("homepage.html") 

@app.route('/verify',methods = ["POST"])
def verify():
    email = request.form["email"]
    message = Mail(
    from_email='nihar@centroxy.com',
    to_emails=email,
    subject='Sending with Twilio SendGrid is Fun',
    html_content='and easy to do anywhere, even with Python')
    html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       """ +str(otp)+ """
    </p>
  </body>
</html>
"""
    
    msg['From'] = FROM_EMAIL
    msg['To'] = email
    msg['Subject'] = "Sendgrid OTP"

    apikey= "apikey"
    password=SENDGRID_API_KEY
    msg.attach(MIMEText(html, 'html'))
    server = smtplib.SMTP('smtp.sendgrid.net: 587')
    server.starttls()
    server.login(apikey, password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    return render_template('verify.html')
    # server.quit()

@app.route('/validate',methods=["POST"])   
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3> Email  verification is  successful </h3>"  
    return "<h3>failure, OTP does not match</h3>"   

if __name__ == '__main__':  
    app.run(debug = True) 