# put your views here

from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import View
from thoughtEngine.blog.models import  Post, Comment



blog = Blueprint('blog', __name__, template_folder='templates')



@blog.route('/')
def  viewList():
    
    posts = Post.objects.all()
    return render_template('blog/list.html', posts=posts)

    
@blog.route('/<title>')
def viewPost(title):
    post = Post.objects.get_or_404(title=title)
    return render_template('blog/detail.html', post=post)

@blog.route('/createPost')
def createPost():
	return render_template('blog/createPost.html')



