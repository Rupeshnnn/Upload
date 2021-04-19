from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SECRET_KEY'] = '123456789'
loginmanager = LoginManager(app)
loginmanager.login_view='login'


from make.models import BasicDetails,EduCa,Personal,Family,Describe
from make import routes

