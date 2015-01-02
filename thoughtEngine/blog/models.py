import datetime
from flask import url_for
from thoughtEngine import db




class User(db.Document):

    email = db.EmailField(max_length=100, required=True, unique=True)
    password = db.StringField(max_length=15, required=True)
    name = db.StringField(max_length=100, required=True)
    registerd_on = db.DateTimeField(default=datetime.datetime.now, required=True)

    # getting  "self.email object has no attribute '_data' "
    # lets instantiate the objects without the use of constructor
    # def __init__(self , email ,password , name):
    #     self.email = email
    #     self.password = password
    #     self.name = name
    
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)


class Comment(db.EmbeddedDocument):
    
    text = db.StringField(max_length=200)
    # user_ref = db.ReferenceField(User)

# this complexity is not necessary at this moment
# class Tag(db.EmbeddedDocument):
#     text = db.StringField(max_length=26)




class Post(db.Document):
    
    """
      blog post content (future to include a filed for images)
    """

    created_by = db.ReferenceField(User)

    title = db.StringField(max_length=100, required=True)
    body  = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    # if false then private else it is public
    visibility = db.BooleanField(default=False)
    tags = db.ListField()
    comments = db.ListField(db.EmbeddedDocumentField(Comment))
    postImage = db.URLField()
    #images = db.ListField(db.FileField())

    
        


    


