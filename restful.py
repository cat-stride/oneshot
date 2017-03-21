# from flask_restful import Resource, reqparse, fields, marshal_with
# from datetime import datetime
# from app.models import Bullet, User
# from . import db

# parser = reqparse.RequestParser()
# parser.add_argument('admin', type=bool, help='Use super manager mode', default=False)

# resource_fields = {
# 	'id': fields.Integer,
# 	'type': fields.String,
# 	'content': fields.String,
# 	'timestamp': fields.DateTime
# }

# class UserResource(Resource):
# 	@marshal_with(resource_fields)
# 	def get(self,id=None):
# 		if id == None:
# 			bullets = Bullet.query.order_by(Bullet.timestamp.desc()).all()
# 		else:
# 			bullets = Bullet.query.filter_by(id=id).all()
# 		ble = {}
# 		rep = []
# 		for bullet in bullets:
# 			ble['id'] = bullet.id
# 			ble['type'] = bullet.type
# 			ble['content'] = bullet.content
# 			ble['timestamp'] = bullet.timestamp
# 			ble['user_id'] = bullet.user_id
# 			rep.append(ble)
# 		return rep


# 	def put(self, id, data):
# 		old_bullet = Bullet.query.get(id)
# 		old_bullet.type = data['type']
# 		old_bullet.content = data['content']
# 		old_bullet.timestamp = datetime.strptime(data['date'],'%Y/%m/%d %H:%M:%S')
# 		db.session.add(old_bullet)
# 		db.session.commit()

# 	def post(self, data):
# 		new_bullet = Bullet(sym_name=data['sym_name'],content=data['content'],\
# 		timestamp=datetime.strptime(data['date'],'%Y/%m/%d %H:%M:%S'))
# 		db.session.add(new_bullet)
# 		db.session.commit()
# 		return new_bullet.id

# 	def delete(self, id):
# 		old_bullet = Bullet.query.get(id)
# 		db.session.delete(old_bullet)
# 		db.session.commit()
