from flask import Blueprint,render_template

views=Blueprint('views',__name__)

@views.route('/')
def mainroute():
    return '<h1>First Page</h1>'

@views.route('/login')
def login():
    return '<h1>Login Page</h1>'