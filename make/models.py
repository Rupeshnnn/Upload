from make import db
from make import loginmanager
from flask_login import UserMixin


@loginmanager.user_loader
def user_loader(user_id):
    return BasicDetails.query.get(int(user_id))


class BasicDetails(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    firstname = db.Column(db.String(120), unique=True, nullable=False)
    midname = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    mobileno = db.Column(db.String(120), unique=True, nullable=False)



class EduCa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    educationlevel=db.Column(db.String(60),nullable=False)
    educationfeild=db.Column(db.String(120),nullable=False)
    Workwith=db.Column(db.String(60),nullable=False)
    workingat=db.Column(db.String(60),nullable=False)
    salary=db.Column(db.String(60),nullable=False)

class Personal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profilefor = db.Column(db.String(60), nullable=False)
    citizenshipno= db.Column(db.String(60), nullable=False)
    maritalstatus = db.Column(db.String(60), nullable=False)
    dateofbirth = db.Column(db.String(60), nullable=False)
    height = db.Column(db.String(60), nullable=False)
    weight = db.Column(db.String(60), nullable=False)
    cast = db.Column(db.String(60), nullable=False)
    religion = db.Column(db.String(60), nullable=False)
    skincolor = db.Column(db.String(60), nullable=False)
    mothertongue = db.Column(db.String(60), nullable=False)






class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    familyvalue=db.Column(db.String(60),nullable=False)
    familytype=db.Column(db.String(60),nullable=False)
    familystatus=db.Column(db.String(60),nullable=False)
    fatheroccupation=db.Column(db.String(60),nullable=False)
    motheroccupation=db.Column(db.String(60),nullable=False)
    brother=db.Column(db.String(60),nullable=False)
    sister=db.Column(db.String(60),nullable=False)

class Describe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    decribe=db.Column(db.String(3000),nullable=False)


