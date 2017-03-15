from app.models import Bullets, User
from . import db



# def create_todolist(tablename, data):
def create_bullet(data):
	bullet = Bullets(body=data['body'])
	db.session.add(bullet)

def read_bullet(bid=None):
	if bid == None:
		bullet = Bullets.query.order_by(Bullets.timestamp.desc()).all()
	else:
		bullet = Bullets.query.filter_by(Bullets.bid=bid).all()
	return bullet

def update_bullet(tablename, data):
	pass

def delete_bullet(tablename, data):
	pass

