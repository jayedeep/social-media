from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
db=SQLAlchemy()

def createapp():
    #initializing app
    app=Flask(__name__)

    #congigurations
    app.config['SECRET_KEY']='Hello'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    #DB settup
    db.init_app(app)
    loginmaneger=LoginManager(app)
    loginmaneger.login_view='/'

    # creating models
    from .models import Users
    createdatabse(app)
    @loginmaneger.user_loader
    def userloader(id):
        return Users.query.filter_by(id=int(id)).first()


    #loading all the routes
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    # return app
    return app

def createdatabse(app):
    if not path.exists('website/database.db'):
        db.create_all(app=app)