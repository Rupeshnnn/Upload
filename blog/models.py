from wtforms import ValidationError

from blog import db
from blog import login_manager
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


# class User:
#     def __init__(self,name,password):
#         self.name = name
#         self.password= password
#
#
#     def show_my_profile(self):
#         print('The user is viewing their profile')
#
#     def create_new_profile(self):
#         print('The user is creating new profile')
#
#
# user=User('Username','Userpassword')
# print('Username=',user.name)
# print('Username=',user.password)
# user.show_my_profile()
# user.create_new_profile()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)

    posts= db.relationship('Post',backref='author')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text(500),  nullable=False)
    #dated_posted= db.Column(db.DateTime,default =datetime.now)
    date_posted = db.Column(db.DateTime,default=datetime.now)
    user_id= db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    #deleted = db.Column(db.Boolean())


class PostBackup(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(150), nullable=False)
     content = db.Column(db.Text(500),  nullable=False)
    #dated_posted= db.Column(db.DateTime,default =datetime.now)
     date_posted = db.Column(db.DateTime,default=datetime.now)
     user_id= db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
