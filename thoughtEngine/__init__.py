from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager



app=Flask(__name__)


app.config["MONGODB_SETTINGS"] = {'DB': "my_thought_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
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