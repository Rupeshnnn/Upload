from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from numpy.compat import unicode
from wtforms import StringField, PasswordField, SelectField, IntegerField, SubmitField, DateField, RadioField, FileField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from make import BasicDetails


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstname = StringField('First_Name', validators=[DataRequired(), Length(min=2, max=30)])
    midname = StringField('Mid_Name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last_name', validators=[DataRequired(), Length(min=2, max=30)])
    gender =SelectField('Gender',choices=[('m','Male'),('f','Female')],validate_choice=True)
    country=SelectField('Country',choices=[('a','America'),('a1','Arab'),('a3','Afganistan'),('a4','Algeria'),('a5','Armania')],validate_choice=True)
    city = SelectField('City',choices=[('K','Kathmandu'),('B','Biratnagar'),('p','Pokhara')],validate_choice=True)
    mobileno=IntegerField('MobileNo',validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def valid_email(self,email):
        em= BasicDetails.query.filter_by(email=email.data).first()
        if em:
            raise ValidationError("Email is taken ,Please chose another one")


class EduCaForm(FlaskForm):
    educationlevel=SelectField("Education-Level:",choices=[('a','below-10'),('b','SLC/SEE'),('c','+2'),('d','Bachelor'),('e','Master'),('f','PDH'),('e','DR.')])
    educationfeild=SelectField("Education-Field:",choices=[('a','Engineering'),('b','CSIT'),('b',"IT"),('c','BCA'),('d','BBA'),('e','MBA'),('f','BSC.Physics'),('g','BSC.Chemistry'),('h','MBBBS'),('i','Agriculture'),('j','Forestry'),('k','None')])
    Workwith=SelectField("Work With:",choices=[('a','NotWorking'),('b','Goverment'),('c','Private-company'),('d','Own-Bussiness')])
    workingat=SelectField("Work As:",choices=[('a','Engineer'),('b','Doctor'),('b','Pilot'),('c','Lawyer'),('d','Officer'),('e','manager'),('f','Progammer'),('g','Administrator'),('h','labor'),('i','Driver'),('j','Cook'),('k','clerk')])
    salary=IntegerField("Salary-Monthly:",validators=[DataRequired()])
    submit=SubmitField("Submit")

class PersonalForm(FlaskForm):
    profilefor =SelectField("ProfileFor", choices=[('s', 'Self'), ('b', 'Brother'), ('f', 'Friend'), ('s', 'Sister'), ('o', 'Other')])
    citizenshipno=IntegerField("Citizenship-No",validators=[DataRequired()])
    maritalstatus=SelectField("MaritalStatus",choices=[('n','Never'),('d','Divorced'),('y',('Yes'))])
    dateofbirth=DateField('DateOfBirth',format='%Y-%m-%d')
    height=IntegerField("Height",validators=[DataRequired()])
    weight=IntegerField("Weight",validators=[DataRequired()])
    cast=SelectField("Cast",choices=[('b','Bhramin'),('c','Chettri'),('m','Magar'),('t','Tamang'),('t','Tamang'),('g','Gurng'),('s','Sherpa'),('g','Gurng'),('d','Dalit')])
    religion=SelectField("Religion",choices=[('h','Hindu'),('b','Buddhist'),('c','Christian'),('m','Muslim'),('j','Jain'),('s','Sikh'),('n','Donot-Belive')])
    skincolor=SelectField('SkinColor',choices=[('b','Black'),('d','Dusky'),('f','Fair')])
    mothertongue=SelectField("MotherTongue",choices=[('n','Nepal'),('m','Magar'),('t','Tamang'),('g','Gurng'),('g','Gurng'),('m1','Mailthali'),('t1','Tharu')])
    submit = SubmitField('Sign Up')

class FamilyForm(FlaskForm):
    familyvalue=RadioField('Family-Value:',choices=[('l','Liberal'),('m','Moderate'),('t','Traditional')],coerce=unicode)
    familytype=RadioField("Family-Type:",choices=[('a','Joint-Family'),('b','Nucelear-Family')],coerce=unicode)
    familystatus=RadioField('Family-Status:',choices=[('a','Poor'),('b','Middle'),('c','Rich')],coerce=unicode)
    fatheroccupation=StringField('Father-occupation:',validators=[DataRequired(),Length(min=2,max=30)])
    motheroccupation=StringField('Mother-occupation:',validators=[DataRequired(),Length(min=2,max=30)])
    brother=StringField('No-of-Bother:',validators=[DataRequired()])
    sister=StringField('No-of-Sister:',validators=[DataRequired()])
    submit=SubmitField('Submit')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstname = StringField('First_Name', validators=[DataRequired(), Length(min=2, max=30)])
    midname = StringField('Mid_Name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last_name', validators=[DataRequired(), Length(min=2, max=30)])
    gender = SelectField('Gender', choices=[('m', 'Male'), ('f', 'Female')], validate_choice=True)
    country = SelectField('Country', choices=[('a', 'America'), ('a1', 'Arab'), ('a3', 'Afganistan'), ('a4', 'Algeria'),
                                              ('a5', 'Armania')], validate_choice=True)
    city = SelectField('City', choices=[('K', 'Kathmandu'), ('B', 'Biratnagar'), ('p', 'Pokhara')],
                       validate_choice=True)
    mobileno = IntegerField('MobileNo', validators=[DataRequired()])
    educationlevel=SelectField("Education-Level:",choices=[('a','below-10'),('b','SLC/SEE'),('c','+2'),('d','Bachelor'),('e','Master'),('f','PDH'),('e','DR.')])
    educationfeild=SelectField("Education-Field:",choices=[('a','Engineering'),('b','CSIT'),('b',"IT"),('c','BCA'),('d','BBA'),('e','MBA'),('f','BSC.Physics'),('g','BSC.Chemistry'),('h','MBBBS'),('i','Agriculture'),('j','Forestry'),('k','None')])
    Workwith=SelectField("Work With:",choices=[('a','NotWorking'),('b','Goverment'),('c','Private-company'),('d','Own-Bussiness')])
    workingat=SelectField("Work As:",choices=[('a','Engineer'),('b','Doctor'),('b','Pilot'),('c','Lawyer'),('d','Officer'),('e','manager'),('f','Progammer'),('g','Administrator'),('h','labor'),('i','Driver'),('j','Cook'),('k','clerk')])
    salary=IntegerField("Salary-Monthly:",validators=[DataRequired()])
    submit=SubmitField("Submit")
    profilefor = SelectField("ProfileFor", choices=[('s', 'Self'), ('b', 'Brother'), ('f', 'Friend'), ('s', 'Sister'),
                                                    ('o', 'Other')])
    citizenshipno = IntegerField("Citizenship-No", validators=[DataRequired()])
    maritalstatus = SelectField("MaritalStatus", choices=[('n', 'Never'), ('d', 'Divorced'), ('y', ('Yes'))])
    dateofbirth = DateField('DateOfBirth', format='%Y-%m-%d')
    height = IntegerField("Height", validators=[DataRequired()])
    weight = IntegerField("Weight", validators=[DataRequired()])
    cast = SelectField("Cast",
                       choices=[('b', 'Bhramin'), ('c', 'Chettri'), ('m', 'Magar'), ('t', 'Tamang'), ('t', 'Tamang'),
                                ('g', 'Gurng'), ('s', 'Sherpa'), ('g', 'Gurng'), ('d', 'Dalit')])
    religion = SelectField("Religion", choices=[('h', 'Hindu'), ('b', 'Buddhist'), ('c', 'Christian'), ('m', 'Muslim'),
                                                ('j', 'Jain'), ('s', 'Sikh'), ('n', 'Donot-Belive')])
    skincolor = SelectField('SkinColor', choices=[('b', 'Black'), ('d', 'Dusky'), ('f', 'Fair')])
    mothertongue = SelectField("MotherTongue",
                               choices=[('n', 'Nepal'), ('m', 'Magar'), ('t', 'Tamang'), ('g', 'Gurng'), ('g', 'Gurng'),
                                        ('m1', 'Mailthali'), ('t1', 'Tharu')])
    familyvalue = RadioField('Family-Value:', choices=[('l', 'Liberal'), ('m', 'Moderate'), ('t', 'Traditional')],
                             coerce=unicode)
    familytype = RadioField("Family-Type:", choices=[('a', 'Joint-Family'), ('b', 'Nucelear-Family')], coerce=unicode)
    familystatus = RadioField('Family-Status:', choices=[('a', 'Poor'), ('b', 'Middle'), ('c', 'Rich')], coerce=unicode)
    fatheroccupation = StringField('Father-occupation:', validators=[DataRequired(), Length(min=2, max=30)])
    motheroccupation = StringField('Mother-occupation:', validators=[DataRequired(), Length(min=2, max=30)])
    brother = StringField('No-of-Bother:', validators=[DataRequired()])
    sister = StringField('No-of-Sister:', validators=[DataRequired()])
    submit = SubmitField('Submit')



class aaaForm(FlaskForm):
    picture = FileField('Picture', validators=[FileAllowed(['jpeg', 'jpg', 'png'])])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstname = StringField('First_Name', validators=[DataRequired(), Length(min=2, max=30)])
    midname = StringField('Mid_Name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last_name', validators=[DataRequired(), Length(min=2, max=30)])
    gender = SelectField('Gender', choices=[('m', 'Male'), ('f', 'Female')], validate_choice=True)
    country = SelectField('Country', choices=[('a', 'America'), ('a1', 'Arab'), ('a3', 'Afganistan'), ('a4', 'Algeria'),
                                              ('a5', 'Armania')], validate_choice=True)
    city = SelectField('City', choices=[('K', 'Kathmandu'), ('B', 'Biratnagar'), ('p', 'Pokhara')],
                       validate_choice=True)
    mobileno = IntegerField('MobileNo', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def valid_email(self, email):
        if current_user.email != self.email.data:
            em = BasicDetails.query.filter_by(email=email.data).first()
            if em:
               raise ValidationError("Email is taken ,Please chose another one")




class profileForm(FlaskForm):
    picture = FileField('Picture', validators=[FileAllowed(['jpeg', 'jpg', 'png'])])

