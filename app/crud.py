from datetime import datetime
from app.models import Bullets, Users
from . import db

 
def create_bullet(data):
	new_bullet = Bullets(sym_name=data['sym_name'],content=data['content'],\
		timestamp=datetime.strptime(data['date'],'%Y/%m/%d %H:%M:%S'))
	db.session.add(new_bullet)
	db.session.commit()
	return new_bullet.bid

def read_bullet(bid=None):
	if bid == None:
		bullet = Bullets.query.order_by(Bullets.timestamp.desc()).all()
	else:
		bullet = Bullets.query.filter_by(bid=bid).all()
	return bullet

def update_bullet(bid, data):
	old_bullet = Bullets.query.get(bid)
	old_bullet.sym_name = data['sym_name']
	old_bullet.content = data['content']
	old_bullet.timestamp = datetime.strptime(data['date'],'%Y/%m/%d %H:%M:%S')
	db.session.add(old_bullet)
	db.session.commit()


def delete_bullet(bid):
	old_bullet = Bullets.query.get(bid)
	db.session.delete(old_bullet)
	db.session.commit()
