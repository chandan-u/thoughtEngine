import datetime
from flask import url_for
from thoughtEngine import db



class User(db.Document):

	emailId = db.EmailField(max_length=100, required=True, unique=True)
	password = db.StringField(max_length=15, required=True)
	name = db.StringField(max_length=100, required=True)

    posts = db.ListField(ReferenceField(Post))

class Post(db.Document):
    
    #content (future to include a filed for images)
    title = db.StringField(max_length=100, required=True)
    body  = db.StringField(required=True)
    
    # if false then private else it is public
    visibility = db.BooleanField(default=False)
    tags = db.ListField(EmbeddedDocumentField(Tag))
    comments = ListField(EmbeddedDocumentField(Comment))


class Comment(db.EmbeddedDocument):
	
	text = db.StringField(max_length=200)
    user_ref = db.ReferenceField(User)

class Tag(db.EmbeddedDocument):
	text = db.StringField(max_length=26)


