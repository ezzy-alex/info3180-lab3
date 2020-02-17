from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alex123'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'bed5c201ff9531'
app.config['MAIL_PASSWORD'] = 'b31c16aa652392'
mail = Mail(app)
from app import views