from flask import Flask

def createapp():
    #initializing app
    app=Flask(__name__)
    #loading all the routes
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    # return app
    return app