import time
from app.models import Bullet, User
from . import db

def register_by_wechat(wechat_id):
	# WEB 端注册时，填写微信号？ 但微信 WEB API 无法获取微信号，只能为每个新增好友设置别名，通过唯一的别名来区别，
	#但当用户在WEB端填写时，怎么知道程序要将他别名设置为什么？
	# 自动注册邮箱？统一为 微信别名@oneshot.com 格式?
	# WEB 端可用 微信别名 登陆？
	new_user = User()
	new_user.mail = wechat_id + "@oneshot.com"
	new_user.username = wechat_id
	new_user.password = wechat_id
	new_user.confirmed = 't'
	new_user.wechat_id = wechat_id
	new_user.register_source = 'wechat'
	db.session.add(new_user)
	db.session.commit()

	rep = {
		'id': new_user.id,
		'mail': new_user.mail,
		'username': new_user.username
	}
	return rep

def find_userid_by_wechatid(wechat_id):
	user = User.query.filter_by(wechat_id=wechat_id).all() # list

	if len(user) > 1:
		print('>1')
		rt = 'User duplicate'
		return None
	elif len(user) < 1:
		print('<1')
		rt = register_by_wechat(wechat_id)
		return rt
	else:
		print('==1')
		rt = {
			'id': user[0].id,
			'mail': user[0].mail,
			'username': user[0].username
		}	
		return rt

def creat_by_wechat(data):
	# user = find_userid_by_wechatid(data['user_id'])
	# if len(user) == 0:
	# 	return -1
	new_bullet = Bullet(type=data['type'], content=data['content'],\
		timestamp=int(time.time()),user_id = data['user_id'])
	db.session.add(new_bullet)
	db.session.commit()
	rep = {
		'id': new_bullet.id,
		'type': new_bullet.type,
		'content': new_bullet.content,
		'timestamp': new_bullet.timestamp,
		'user_id': new_bullet.user_id
	}
	return rep

def read_by_type_wechat(user_id,btype):
	bullets = Bullet.query.filter_by(user_id=user_id,type=btype).order_by(Bullet.timestamp.desc()).all()
	ble = {}
	rep = []
	for bullet in bullets:
		ble['id'] = bullet.id
		ble['type'] = bullet.type
		ble['content'] = bullet.content
		ble['timestamp'] = bullet.timestamp
		ble['user_id'] = bullet.user_id
		rep.append(ble.copy())
	return rep

def read_by_bid_wechat(user_id,bid):
	bullets = Bullet.query.filter_by(user_id=user_id,id=bid).all()
	ble = {}
	rep = []
	for bullet in bullets:
		ble['id'] = bullet.id
		ble['type'] = bullet.type
		ble['content'] = bullet.content
		ble['timestamp'] = bullet.timestamp
		ble['user_id'] = bullet.user_id
		rep.append(ble.copy())
	return rep

def read_date_by_wechat(user_id, timestamp):
	date1 = time.strftime('%Y-%m-%d 00:00:00',time.localtime(int(timestamp)))
	date2 = time.strftime('%Y-%m-%d 23:59:59',time.localtime(int(timestamp)))
	t1 = int(time.mktime(time.strptime(date1,'%Y-%m-%d %H:%M:%S')))
	t2 = int(time.mktime(time.strptime(date2,'%Y-%m-%d %H:%M:%S')))
	bullets = Bullet.query.filter_by(user_id=user_id).\
	filter(Bullet.timestamp > t1).filter(Bullet.timestamp < t2).\
	order_by(Bullet.timestamp.desc()).all()
	ble = {}
	rep = []
	for bullet in bullets:
		ble['id'] = bullet.id
		ble['type'] = bullet.type
		ble['content'] = bullet.content
		ble['timestamp'] = bullet.timestamp
		ble['user_id'] = bullet.user_id
		rep.append(ble.copy())
	return rep

def read_all_by_wechat(user_id):
	bullets = Bullet.query.filter_by(user_id=user_id).order_by(Bullet.timestamp.desc()).all()
	ble = {}
	rep = []
	for bullet in bullets:
		ble['id'] = bullet.id
		ble['type'] = bullet.type
		ble['content'] = bullet.content
		ble['timestamp'] = bullet.timestamp
		ble['user_id'] = bullet.user_id
		rep.append(ble.copy())
	return rep

# def auto_push_bullet_by_wechat(user_id, btype):
# 	bullets = Bullet.query.filter_by(user_id=user_id,type=btype).order_by(Bullet.timestamp.desc()).all()
# 	ble = {}
# 	rep = []
# 	for bullet in bullets:
# 		ble['id'] = bullet.id
# 		ble['type'] = bullet.type
# 		ble['content'] = bullet.content
# 		ble['timestamp'] = bullet.timestamp
# 		ble['user_id'] = bullet.user_id
# 		rep.append(ble.copy())
# 	return rep
