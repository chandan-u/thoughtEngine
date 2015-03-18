# put your views here

from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import View
from thoughtEngine.blog.models import  Post, Comment, User, Journal



from flask import Flask,session,flash, abort ,g
from flask.ext.login import login_user , logout_user , current_user , login_required

from mongoengine.queryset import DoesNotExist

import datetime

blog = Blueprint('blog', __name__, template_folder='templates')








     
# blog related views
@blog.route('/')
def viewList():
    posts = Post.objects.all()
    return render_template('blog/list.html', posts=posts)

    
@blog.route('/<title>')
def viewPost(title):
    post = Post.objects.get_or_404(title=title)
    return render_template('blog/detail.html', post=post)



@blog.route('/createPost')
@login_required
def createPost():
    return render_template('blog/createPost.html')


@blog.route('/savePost', methods=['POST'])
def savePost():
    title = request.form['title']
    content = request.form['content']
    tags_string = request.form['tags']
    tags =tags_string.split(',')

    # pice of code that extracts the first image from the post, and makes it the posts display image.
    # include exceptional handling. if no image is there display title in the place of image.
    # And the value postImage will be set to None.
    import lxml.html as parser
    xhtml = parser.document_fromstring(content)
    if(xhtml.xpath('//img[1]/@src')):
        postImageURL = xhtml.xpath('//img[1]/@src')
        post  = Post(title=title, body=content, tags=tags, postImage=postImageURL[0])
    else:
        post  = Post(title=title, body=content, tags=tags)
    post.save()
    return title


# User registration/login/logout views
@blog.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User()
    user.email = request.form['email']
    user.password= request.form['password']
    user.name = request.form['name']
    user.save()
    # db.session.add(user)
    # db.session.commit()
    # flash('User successfully registered')
    return redirect('/login')
 
#ajax request
@blog.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':     
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']

    try:
        registered_user = User.objects.get(email=email,password=password)
    except DoesNotExist:
        return 'DoesNotExist'

    login_user(registered_user)
    # flash('Logged in successfully')
    return "exist"


@blog.route('/logout')
def logout():
    logout_user()
    return redirect('/')


# journal views
@blog.route('/journal')
@login_required
def journal():
    journals = Journal.objects(user=current_user.id)
    tags=[]
    for journal in journals:
        for tag in journal.tags:
            if tag not in tags:
                tags.append(tag) 
    return render_template('journal/journal.html', tags=tags)


#ajax request
@blog.route('/saveJourn', methods=['POST'])
@login_required
def saveJournal():
    content = request.form["content"]
    created_on = request.form["created_on"] 
    tagstring = request.form["tagstring"]
    tags = tagstring.split(',')
    # we are getting ISO string from the front end
    journal = Journal(user=current_user.id, created_on= datetime.datetime.strptime(created_on, "%Y-%m-%dT%H:%M:%S.%fZ"), content=content, tags=tags)
    journal.save()
    return "S"


@blog.route('/journal/tagView/<search_tag>', methods=['GET'])
@login_required
def journalTagView(search_tag):
    journals = Journal.objects(user = current_user.id)
    
    
    tags=[]
    for journal in journals:
        for tag in journal.tags:
            if tag not in tags:
                tags.append(tag)
    
    
    tag_journals = Journal.objects(user = current_user.id, tags__contains=search_tag)   
    return render_template('journal/tagView.html', journals=tag_journals, tags=tags)

@blog.route('/journal/<journal_id>', methods=['GET'])
@login_required
def viewJournal(journal_id):
    journals = Journal.objects(user = current_user.id)
    tags=[]
    for journal in journals:
        for tag in journal.tags:
            if tag not in tags:
                tags.append(tag)
    journal = Journal.objects.get(pk = journal_id)
    print journal
    return render_template('journal/viewJournal.html', journal=journal, tags=tags )


