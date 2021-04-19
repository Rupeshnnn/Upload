from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rupesh:rupesh123@localhost/project'



db = SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login'
#from blog.models import Student
from blog import routes


