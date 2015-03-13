# put your views here

from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import View
from thoughtEngine.blog.models import  Post, Comment, User

from thoughtEngine import login_manager


from flask import Flask,session,flash, abort ,g
from flask.ext.login import login_user , logout_user , current_user , login_required

from mongoengine.queryset import DoesNotExist

blog = Blueprint('blog', __name__, template_folder='templates')





@login_manager.user_loader
def load_user(id):
    return User.objects.get( pk = id)


     

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
    postImageURL = xhtml.xpath('//img[1]/@src')

    
    post  = Post(title=title, body=content, tags=tags, postImage=postImageURL[0])
    post.save()
    return title

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


@blog.route('/journal')
def jounral():
    return render_template('blog/journal.html')