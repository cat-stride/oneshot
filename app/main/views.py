# coding:utf-8
from flask import render_template,request,redirect,url_for,flash,jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.main import main,errors
from app import crud
import json
import time

# index page
@main.route('/',methods=['GET'])
def index():
	user_id = current_user.get_id()
	posts = crud.read_bullet_by_type(user_id=user_id,type=None)
	return render_template('index.html')

# request and response
@main.route('/api/bullets',methods=['GET'])
def get_bullets():
	user_id = current_user.get_id()
	posts = crud.read_bullet_by_type(user_id=user_id,type=None)
	return jsonify(posts)

@main.route('/api/bullets/<type>',methods=['GET'])
def get_bullets_by_type(type):
	user_id = current_user.get_id()
	posts = crud.read_bullet_by_type(user_id=user_id,type=type)
	return jsonify(posts)


@main.route('/api/bullets/<int:bid>',methods=['GET'])
def get_a_bullet(bid):
	user_id = current_user.get_id()
	posts = crud.read_bullet_by_bid(user_id=user_id, bid=bid)
	return jsonify(posts)

@main.route('/api/bullets', methods=['POST'])
def create_a_bullet():
	user_id = current_user.get_id()
	req = request.get_data(as_text=True)
	print(req)
	b = req.replace("'", "\"")
	body = json.loads(b)
	body['user_id'] = user_id
	rep = crud.create_bullet(body)
	return jsonify(rep)


@main.route('/api/bullets/<int:bid>', methods=['PUT'])
def update_a_bullet(bid):
	user_id = current_user.get_id()
	req = request.get_data().decode('utf-8')
	body = eval(req)
	body['user_id'] = user_id
	rep = crud.update_bullet(bid,body)
	return jsonify(rep)

@main.route('/api/bullets/<int:bid>', methods=['DELETE'])
def delete_a_bullet(bid):
	rep = crud.delete_bullet(bid)
	return jsonify(rep)
