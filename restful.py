# from flask_restful import Resource, reqparse, fields, marshal_with
# from datetime import datetime
# from app.models import Bullets, Users
# from . import db

# parser = reqparse.RequestParser()
# parser.add_argument('admin', type=bool, help='Use super manager mode', default=False)

# resource_fields = {
# 	'bid': fields.Integer,
# 	'sym_name': fields.String,
# 	'content': fields.String,
# 	'timestamp': fields.DateTime
# }

# class UserResource(Resource):
# 	@marshal_with(resource_fields)
# 	def get(self,bid=None):
# 		if bid == None:
# 			bullets = Bullets.query.order_by(Bullets.timestamp.desc()).all()
# 		else:
# 			bullets = Bullets.query.filter_by(bid=bid).all()
# 		ble = {}
# 		rep = []
# 		for bullet in bullets:
# 			ble['bid'] = bullet.bid
# 			ble['sym_name'] = bullet.sym_name
# 			ble['content'] = bullet.content
# 			ble['timestamp'] = bullet.timestamp
# 			ble['uid'] = bullet.uid
# 			rep.append(ble)
# 		return rep


# 	def put(self, bid, data):
# 		old_bullet = Bullets.query.get(bid)
# 		old_bullet.sym_name = data['sym_name']
# 		old_bullet.content = data['content']
# 		old_bullet.timestamp = datetime.strptime(data['date'],'%Y/%m/%d %H:%M:%S')
# 		db.session.add(old_bullet)
# 		db.session.commit()

# 	def post(self, data):
# 		new_bullet = Bullets(sym_name=data['sym_name'],content=data['content'],\
# 		timestamp=datetime.strptime(data['date'],'%Y/%m/%d %H:%M:%S'))
# 		db.session.add(new_bullet)
# 		db.session.commit()
# 		return new_bullet.bid

# 	def delete(self, bid):
# 		old_bullet = Bullets.query.get(bid)
# 		db.session.delete(old_bullet)
# 		db.session.commit()
