# coding:utf-8
from flask import render_template,request,redirect,url_for,flash,jsonify
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
	return json.dumps(posts)

@main.route('/api/bullets/<int:bid>',methods=['GET'])
def get_a_bullet(bid):
	posts = crud.read_bullet(bid)
	return render_template('index.html', posts=posts)


@main.route('/api/bullets', methods=['POST'])
def create_a_bullet():
	req = request.get_data().decode('utf-8') # str
	body = eval(req)
	bid = crud.create_bullet(body)
	rep = {
		'bid': bid,
		'sym_name': body['sym_name'],
		'content': body['content'],
		'date': body['date']
	}
	return jsonify(rep)


@main.route('/api/bullets/<int:bid>', methods=['PUT'])
def update_a_bullet(bid):
	req = request.get_data().decode('utf-8')
	body = eval(req)
	crud.update_bullet(bid,body)
	rep = {
		'bid': bid,
		'sym_name': body['sym_name'],
		'content': body['content'],
		'date': body['date']
	}
	return jsonify(rep)

@main.route('/api/bullets/<int:bid>', methods=['DELETE'])
def delete_a_bullet(bid):
	crud.delete_bullet(bid)
	return 'h'


# #sign up
# @main.route('/signup',methods=['GET','POST'])
# def signup():
# 	pass

# #sign in
# @main.route('/signin',methods=['GET','POST'])
# def signin():
# 	pass

