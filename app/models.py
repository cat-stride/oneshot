# coding:utf-8
from . import db
from datetime import datetime

class Bullets(db.Model):
	"""todolist table"""
	__tablename__ = 'bullet'
	bid = db.Column(db.Integer, primary_key=True)
	sym_name = db.Column(db.Text, nullable=False)
	content = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
	uid = db.Column(db.Integer, db.ForeignKey('user.uid'))


class User(db.Model):
	"""user table"""
	__tablename__ = 'user'
	uid = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(10),nullable=False, index=True, unique=True)
	true_name = db.Column(db.String(10))
	sex = db.Column(db.String(2))
	birthday = db.Column(db.DateTime)
	location = db.Column(db.Text)
	email = db.Column(db.String(100),nullable=False, unique=True)
	password_md5 = db.Column(db.Text)
	signup_datetime = db.Column(db.DateTime)
	last_signin_datetime = db.Column(db.DateTime)
