# coding:utf-8
from flask import render_template,request,redirect,url_for,flash,jsonify
from app.main import main,errors
from app import crud
import json
import time

# index page
@main.route('/',methods=['GET'])
def index():
	posts = crud.read_bullet()
	return render_template('index.html')

# request and response
@main.route('/api/bullets',methods=['GET'])
def get_bullets():
	posts = crud.read_bullet()
	return jsonify(posts)

@main.route('/api/bullets/<int:id>',methods=['GET'])
def get_a_bullet(id):
	posts = crud.read_bullet(id)
	return jsonify(posts)

@main.route('/api/bullets', methods=['POST'])
def create_a_bullet():
	req = request.get_data(as_text=True)
	print(req)
	b = req.replace("'", "\"")
	# d = json.JSONDecoder(b)
	body = json.loads(b)
	rep = crud.create_bullet(body)
	return jsonify(rep)


@main.route('/api/bullets/<int:id>', methods=['PUT'])
def update_a_bullet(id):
	req = request.get_data().decode('utf-8')
	body = eval(req)
	rep = crud.update_bullet(id,body)
	return jsonify(rep)

@main.route('/api/bullets/<int:id>', methods=['DELETE'])
def delete_a_bullet(id):
	rep = crud.delete_bullet(id)
	return jsonify(rep)


# #sign up
# @main.route('/signup',methods=['GET','POST'])
# def signup():
# 	pass

# #sign in
# @main.route('/signin',methods=['GET','POST'])
# def signin():
# 	pass
