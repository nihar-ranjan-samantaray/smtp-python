import os
from flask import *  
from flask_mail import *
from random import randint  
app = Flask(__name__)  

app.config["MAIL_SERVER"]= os.getenv('SMTP_GMAIL_SERVER')  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = os.getenv('SMTP_GMAIL_USER')   
app.config['MAIL_PASSWORD'] = os.getenv('SMTP_GMAIL_PASSWORD')   
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)  
otp = randint(000000,999999)   
@app.route('/')  
def index():
    return render_template("homepage.html")  
@app.route('/verify',methods = ["POST"])
def verify():
    email = request.form["email"]   
    msg = Message('OTP',sender = os.getenv('SMTP_GMAIL_FROM_MAIL'), recipients = [email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
@app.route('/validate',methods=["POST"])   
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3> Email  verification is  successful </h3>"  
    return "<h3>failure, OTP does not match</h3>"   

if __name__ == '__main__':  
    app.run(debug = True) 