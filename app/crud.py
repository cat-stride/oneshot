import time
from app.models import Bullet, User
from . import db

def create_bullet(data):
	new_bullet = Bullet(type=data['type'], content=data['content'],\
		timestamp=int(time.time()))
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

def read_bullet(id=None):
	if id == None:
		bullets = Bullet.query.order_by(Bullet.timestamp.desc()).all()
	else:
		bullets = Bullet.query.filter_by(id=id).all()
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

def update_bullet(id, data):
	original_bullet = Bullet.query.get(id)
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

def delete_bullet(id):
	old_bullet = Bullet.query.get(id)
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
