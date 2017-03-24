# coding:utf-8
from flask import render_template,request,redirect,url_for,flash,jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.main import main,errors
from app import crud, crud_by_wechat
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


# wechat api
@main.route('/wechat/api/bullets/register', methods=['POST'])
def register_by_wechat():
	req = request.get_data(as_text=True)
	# print(req)
	body = json.loads(req)
	rep = crud_by_wechat.find_userid_by_wechatid(body['wechat_id'])
	# print('rep:',rep)
	return jsonify(rep)


@main.route('/wechat/api/bullets', methods=['POST'])
def create_bullet_by_wechat():
	req = request.get_data(as_text=True)
	# print(req)
	body = json.loads(req)
	rep = crud_by_wechat.creat_by_wechat(body)
	# print('rep:',rep)
	return jsonify(rep)


@main.route('/wechat/api/bullets/', methods=['GET'])
def get_all_bullet_by_wechat():
	user_id = request.args.get('user_id')
	rep = crud_by_wechat.read_all_by_wechat(user_id)
	return jsonify(rep)

@main.route('/wechat/api/bullets/date/', methods=['GET'])
def get_date_bullet_by_wechat():
	user_id = request.args.get('user_id')
	timestamp = request.args.get('timestamp')
	print(user_id,timestamp)
	rep = crud_by_wechat.read_date_by_wechat(user_id,timestamp)
	return jsonify(rep)

@main.route('/wechat/api/bullets/type/', methods=['GET'])
def get_type_bullet_by_wechat():
	user_id = request.args.get('user_id')
	btype = request.args.get('type')
	print(user_id,btype)
	rep = crud_by_wechat.read_by_type_wechat(user_id,btype)
	return jsonify(rep)

@main.route('/wechat/api/bullets/<int:bid>', methods=['DELETE'])
def delete_bullet_by_wechat(bid):
	pass

@main.route('/wechat/api/bullets/<int:bid>', methods=['PUT'])
def put_bullet_by_wechat(bid):
	pass

@main.route('/wechat/api/bullets/<int:bid>', methods=['GET'])
def get_a_bullet_by_wechat(bid):
	pass