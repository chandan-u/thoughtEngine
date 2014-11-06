import datetime
from flask import url_for
from thoughtEngine import db



class Comment(db.EmbeddedDocument):
    
    text = db.StringField(max_length=200)
    # user_ref = db.ReferenceField(User)

# class Tag(db.EmbeddedDocument):
#     text = db.StringField(max_length=26)

class Post(db.Document):
    
    #content (future to include a filed for images)
    title = db.StringField(max_length=100, required=True)
    body  = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    # if false then private else it is public
    visibility = db.BooleanField(default=False)
    tags = db.ListField()
    comments = db.ListField(db.EmbeddedDocumentField(Comment))



# class User(db.Document):

#     emailId = db.EmailField(max_length=100, required=True, unique=True)
#     password = db.StringField(max_length=15, required=True)
#     name = db.StringField(max_length=100, required=True)
#     posts = db.ListField(db.ReferenceField(Post))

