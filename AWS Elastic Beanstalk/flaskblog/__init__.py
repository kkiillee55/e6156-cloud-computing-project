from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os
app=Flask(__name__)
app.config['SECRET_KEY']='5dd0ca1eb7b10ea76f4d8665f713471053be329151b6cab8b0b369ac1c605415'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

#add more here
login_manager.login_view='login'
login_manager.login_message_category='info'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='zhangliao322@gmail.com'
app.config['MAIL_PASSWORD']='rtyzkwcwlcmcxoew'
mail=Mail(app)
from flaskblog import routes