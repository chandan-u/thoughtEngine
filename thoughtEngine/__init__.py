from flask import Flask
from flask.ext.mongoengine import MongoEngine, connect
from flask.ext.login import LoginManager

import os

MONGO_URL = os.environ.get("MONGOHQ_URL")


if MONGO_URL:
    credentials = re.sub(r"(.*?)//(.*?)(@hatch)", r"\2",MONGO_URL)
    username = credentials.split(":")[0]
    password = credentials.split(":")[1]
    app.config["MONGODB_DB"] = MONGO_URL.split("/")[-1]
    app.config["SECRET_KEY"] = "KeepThisS3cr3t"
    connect(
        MONGO_URL.split("/")[-1],
        host=MONGO_URL,
        port=29257,
        username=username,
        password=password
    )

app=Flask(__name__)


#app.config["MONGODB_SETTINGS"] = {'DB': "my_thought_log", 'host':'', 'port':'', 'user': '', 'password': ''}

app.jinja_env.autoescape = False
db = MongoEngine(app)

# implement login manager for flask-login extension
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

def register_blueprints(app):
    # Prevents circular imports
    from thoughtEngine.blog.views import blog
    app.register_blueprint(blog)

register_blueprints(app)


if __name__=='__main__':
    app.run()
