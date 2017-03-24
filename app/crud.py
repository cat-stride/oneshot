import time
from app.models import Bullet, User
from . import db


def create_bullet(data):
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

def read_bullet_by_type(user_id,type=None):
	if type == None:
		bullets = Bullet.query.filter_by(user_id=user_id).order_by(Bullet.timestamp.desc()).all()
	else:
		bullets = Bullet.query.filter_by(user_id=user_id,type=type).all()
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

def read_bullet_by_bid(user_id,bid=None):
	if bid == None:
		bullets = Bullet.query.filter_by(user_id=user_id).order_by(Bullet.timestamp.desc()).all()
	else:
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

def update_bullet(bid, data):
	original_bullet = Bullet.query.get(bid)
	original_bullet.type= data['type']
	original_bullet.content = data['content']
	original_bullet.timestamp = int(time.time())
	db.session.add(original_bullet)
	db.session.commit()
	rep = {
		'id': original_bullet.id,
		'type': original_bullet.type,
		'content': original_bullet.content,
		'timestamp': original_bullet.timestamp,
		'user_id': original_bullet.user_id
	}
	return rep

def delete_bullet(bid):
	old_bullet = Bullet.query.get(bid)
	db.session.delete(old_bullet)
	db.session.commit()
	rep = {
		'id': old_bullet.id,
		'type': old_bullet.type,
		'content': old_bullet.content,
		'timestamp': old_bullet.timestamp,
		'user_id': old_bullet.user_id
	}
	return rep
