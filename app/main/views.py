# coding:utf-8
from flask import render_template,request,redirect,url_for,flash
from app.main import main
from app import crud
import json

# index page
@main.route('/',methods=['GET','POST'])
@main.route('/index',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		data = {}
		content = request.form['anything']
		data['body'] = content
		# data['user_id'] = 1
		crud.create_bullet(data)
		return redirect(url_for('.index'))
	else:
		posts = crud.read_bullet()
		return render_template('index.html', posts=posts)
		

# request and response
@main.route('/api/bullets',methods=['GET'])
def get_bullets():
	posts = crud.read_bullet()
	return render_template('index.html', posts=posts)

@main.route('/api/bullets/<int:bid>',methods=['GET'])
def get_a_bullet(bid):
	posts = crud.read_bullet(bid)
	return render_template('index.html', posts=posts)


@main.route('/api/bullets/<int:bid>', methods=['POST'])
def create_a_bullet(bid):
	crud.create_bullet()


@main.route('/api/bullets/<int:bid>', methods=['PUT'])
def update_a_bullet(bid):
	crud.update_bullet(bid)

@main.route('/api/bullets/<int:bid>', methods=['DELETE'])
def update_a_bullet(bid):
	crud.delete_bullet(bid)


# #sign up
# @main.route('/signup',methods=['GET','POST'])
# def signup():
# 	pass

# #sign in
# @main.route('/signin',methods=['GET','POST'])
# def signin():
# 	pass

