import time
from app.models import Bullets, Users
from . import db

 
def create_bullet(data):
	new_bullet = Bullets(sym_name=data['sym_name'],content=data['content'],\
		timestamp=int(time.time()))
	db.session.add(new_bullet)
	db.session.commit()
	rep = {
		'bid': new_bullet.bid,
		'sym_name': new_bullet.sym_name,
		'content': new_bullet.content,
		'timestamp': new_bullet.timestamp,
		'uid': new_bullet.uid
	}
	return 	rep

def read_bullet(bid=None):
	if bid == None:
		bullets = Bullets.query.order_by(Bullets.timestamp.desc()).all()
	else:
		bullets = Bullets.query.filter_by(bid=bid).all()
	ble = {}
	rep = []
	for bullet in bullets:
		ble['bid'] = bullet.bid
		ble['sym_name'] = bullet.sym_name
		ble['content'] = bullet.content
		ble['timestamp'] = bullet.timestamp
		ble['uid'] = bullet.uid
		rep.append(ble.copy())
	return rep

def update_bullet(bid, data):
	original_bullet = Bullets.query.get(bid)
	original_bullet.sym_name = data['sym_name']
	original_bullet.content = data['content']
	original_bullet.timestamp = int(time.time())
	db.session.add(original_bullet)
	db.session.commit()
	rep = {
		'bid': original_bullet.bid,
		'sym_name': original_bullet.sym_name,
		'content': original_bullet.content,
		'timestamp': original_bullet.timestamp,
		'uid': original_bullet.uid
	}
	return rep

def delete_bullet(bid):
	old_bullet = Bullets.query.get(bid)
	db.session.delete(old_bullet)
	db.session.commit()
	rep = {
		'bid': old_bullet.bid,
		'sym_name': old_bullet.sym_name,
		'content': old_bullet.content,
		'timestamp': old_bullet.timestamp,
		'uid': old_bullet.uid
	}
	return rep
