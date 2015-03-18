from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
from flask.ext.login import LoginManager
# from thoughtEngine.blog.views import load_user

import os
import re


app=Flask(__name__)



# establish connection with the DB

MONGO_URL = os.environ.get("MONGOHQ_URL")
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS=os.environ.get("MONGO_PASS")

if MONGO_URL:
    #credentials = re.sub(r"(.*?)//(.*?)(@hatch)", r"\2",MONGO_URL)
    #username = credentials.split(":")[1]
    #password = credentials.split(":")[2]
    app.config["MONGODB_DB"] = MONGO_URL.split("/")[-1]
    app.config["SECRET_KEY"] = "KeepThisS3cr3t"
    app.config["MONGODB_HOST"]=MONGO_URL
    app.config["MONGODB_PORT"]=29257
    app.config["MONGODB_USERNAME"]=MONGO_USER
    app.config["MONGODB_PASSWORD"]=MONGO_PASS 
    # app.config["MONGODB_SETTINGS"] = {'DB': "my_thought_log"}
     


app.jinja_env.autoescape = False  
db = MongoEngine(app)



# implement login manager for flask-login extension
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
#login_manager.user_loader(load_user)


#set Debug config:
app.config['DEBUG'] = True


def register_blueprints(app):
    # Prevents circular imports
    from thoughtEngine.blog.views import blog
    app.register_blueprint(blog)

register_blueprints(app)


if __name__=='__main__':
    app.run()
