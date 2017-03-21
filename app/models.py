# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager
import time

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	mail = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	confirmed = db.Column(db.Boolean, default=False)
	bullets = db.relationship('Bullet', backref='user', lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id})

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		db.session.add(self)
		return True

	def __repr__(self):
		return '<User %r>' % self.username

class Bullet(db.Model):
	__tablename__ = 'bullets'
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(64), nullable=False)#, unique=True)
	content = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.Integer, nullable=False, index=True, default=int(time.time()))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
