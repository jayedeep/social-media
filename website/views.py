from flask import Blueprint,render_template,request,redirect,url_for
from .models import Users
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,login_user,logout_user
from . import db
views=Blueprint('views',__name__)

@views.route('/')
def mainroute():
    return '<h1>abc</h1>'

@views.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        username_exiest=Users.query.filter_by(username=username).first()
        email_exiest =Users.query.filter_by(email=email).first()

        if password != password2:
            print("Password Doesn't match")
        elif username_exiest or email_exiest:
            print("User already exiest")
        elif len(password) <6 or len(username) <6:
            print("Username or Password is too short")
        else:
            new_user=Users(username=username,email=email,password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('views.posts'))

    return render_template('register.html')

@views.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=Users.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user)
                print("Logged In")
                return redirect(url_for('views.posts'))

            else:
                print("wrong password")
        else:
            print("username does'nt exiest")
    return render_template('login.html')


@login_required
@views.route('/posts')
def posts():
    return '<h1>Welcome to POST</h1>'


@login_required
@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.mainroute'))