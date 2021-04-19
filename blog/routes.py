import os

from flask_wtf import form
from sqlalchemy.sql.functions import user

from blog import app,db
from flask import render_template, redirect, flash, session, url_for,abort,request
from flask_login import login_user, current_user, login_required,logout_user
from blog.forms import RegistrationForm, LoginForm, ProfileupdateForm, PostForm
from blog.models import User, Post, PostBackup
D


@app.route("/")
def home():
    try:
        my_page =int(request.args.get('my_page',1))
    except Exception:
        abort(404)
    posts= Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3,page=my_page)
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title_name='about_page')

@app.route("/registration",methods=["GET","POST"])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'New account has been created','success')
        return redirect("/")
    return render_template('registration.html',form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        print(user)

        if user and user.password ==form.password.data:
            login_user(user)
            flash(f'Login Sucessful','success')
            return redirect("/")


        else:
            flash(f'Incorrect email/password','danger')
    return render_template('login.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/profile",methods=["POST","GET"])
@login_required
def profile():
    form = ProfileupdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            filename,extension=os.path.splitext(form.picture.data.filename)
            new_file_name = current_user.username + extension
            file_path=os.path.join(app.root_path, 'static/profile_pictures',new_file_name)
            # blog/static/profile picture/Ram1.jpg
            form.picture.data.save(file_path)
            current_user.image_file = new_file_name
            print("exten====",extension)
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.add(current_user)
        db.session.commit()
        flash(f"Your account has been updated","success")
        return redirect("/profile")
    form.username.data = current_user.username
    form.email.data = current_user.email
    return render_template("profile.html",name_title="profile",form = form)


@app.route('/post/new',methods=["GET","POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data,content=form.content.data,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('your new post is created', 'success')
        return redirect(url_for('home'))
    return render_template("create_post.html",title_name = 'create_post',form= form,legend="New_post")


@app.route("/post/<int:post_id>") # post/1 or post/2
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', post=post, title_name='post Detail')

@app.route("/post/<int:post_id>/update",methods=["GET","POST"])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.id != post.user_id:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('post',post_id = post.id))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('create_post.html',form = form,title_name='update post',legend='update_post')



@app.route("/post/<int:post_id>/delete",methods=["GET","POST"])
def delete_post(post_id):
     post = Post.query.get_or_404(post_id)
     if current_user.id != post.user_id:
         abort(403)
     # post.deleted = True
     # db.session.commit()
     # return redirect(url_for("home"))

     post_backup=PostBackup(title=post.title,content=post.content,date_posted=post.date_posted,user_id=post.user_id)
     db.session.add(post_backup)
     db.session.commit()
     flash(f"Your post is deleted","success")
     return redirect((url_for("home")))


@app.route('/search',methods=["GET","POST"])
def search():
    page = request.args.get('my_page',1,type=int)
    if request.method=='POST':
        search_word = request.form['search']
        session['search']=search_word
    if 'search' in session:
        posts = Post.query.filter(Post.title.ilike(f'%{session["search"]}%')).paginate(per_page=3,page=page)
    else:
        posts =Post.query.paginate(per_page=3,page=page)
    return render_template('search_page.html',posts=posts,title_name='search',search_word=session.get('search'))
