from flask import session, render_template, flash
from werkzeug.utils import redirect
from flask_login import login_user, current_user, logout_user,login_required
from make import app, db, BasicDetails
#from make.forms import RegistrationForm, EduCaForm, FamilyForm, PersonalForm, LoginForm
from make.forms import RegistrationForm, EduCaForm, PersonalForm, FamilyForm, LoginForm, UpdateForm, aaaForm, \
    profileForm
from make.models import BasicDetails, EduCa, Family, Personal



@app.route("/")
def home():
    print(session)

    return render_template('home.html',tittle='Home-Page')



@app.route("/registration" ,methods=["GET","POST"])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
          basic_details=BasicDetails(email=form.email.data,password=form.password.data,firstname=form.firstname.data,
          midname=form.midname.data,lastname=form.lastname.data,gender=form.gender.data,country=form.country.data,city=form.city.data,mobileno=form.mobileno.data)

          db.session.add(basic_details)
          db.session.commit()
          return redirect('/education')


    return render_template('registration.html',title_name='registration-Page',form=form)

@app.route("/education",methods=["GET","POST"])
def educa():
    form = EduCaForm()
    if form.validate_on_submit():
        ed=EduCa(educationlevel=form.educationlevel.data,educationfeild=form.educationfeild.data,Workwith=form.Workwith.data,workingat=form.workingat.data,salary=form.salary.data)
        db.session.add(ed)
        db.session.commit()
        return redirect('/family')
    return render_template('EduCa.html',tittle_name='Education_carrer',form=form)

@app.route("/personaldetails",methods=['GET','POST'])
def personal():
    form=PersonalForm()
    if form.validate_on_submit():
        aa=Personal(profilefor=form.profilefor.data,citizenshipno=form.citizenshipno.data,maritalstatus=form.maritalstatus.data,dateofbirth=form.dateofbirth.data,height=form.height.data,weight=form.weight.data,cast=form.cast.data,religion=form.religion.data,skincolor=form.skincolor.data,mothertongue=form.mothertongue.data)
        db.session.add(aa)
        db.session.commit()
        return redirect('/')

    return render_template("personal.html",tittl_name='Personal detail',form=form)

@app.route("/family",methods=['GET','POST'])
def family():
    form =FamilyForm()
    if form.validate_on_submit():
        family=Family(familyvalue=form.familyvalue.data,familytype=form.familytype.data,familystatus=form.familystatus.data,fatheroccupation=form.fatheroccupation.data,motheroccupation=form.motheroccupation.data,brother=form.brother.data,sister=form.sister.data)
        db.session.add(family)
        db.session.commit()
        return redirect('/personaldetails')

    return render_template('Family.html',tittle_name='Personal-info',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       basicdeatils= BasicDetails.query.filter_by(email=form.email.data,password=form.password.data).first()
       print(basicdeatils)
       if basicdeatils is None:
             flash(f'Please enter the right ','danger')
       else:
             login_user(basicdeatils)
             print(f'Login sucessfully')
             return redirect('/profile')

    return render_template('login.html',title_name='login_page',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form = aaaForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.mobileno = form.mobileno.data
        db.session.add(current_user)
        return redirect('/profile')

    form.email.data = current_user.email
    form.mobileno.data = current_user.mobileno
    return render_template('profile.html', form=form)



@app.route('/update',methods=['GET','POST'])
def update():
    pass