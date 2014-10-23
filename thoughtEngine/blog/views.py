# put your views here

from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from thoughtEngine.blog.models import User, Post, Comment


def ListView(request):
	
