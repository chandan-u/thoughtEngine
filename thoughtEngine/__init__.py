from flask import Flask
from flask.ext.mongoengine import MongoEngine




app=Flask(__name__)


app.config["MONGODB_SETTINGS"] = {'DB': "my_thought_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from thoughtEngine.blog.views import blog
    app.register_blueprint(blog)

register_blueprints(app)


if __name__=='__main__':
    app.run()