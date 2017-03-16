# coding:utf-8
from . import db
from datetime import datetime

class Bullets(db.Model):
	"""bullets table"""
	__tablename__ = 'bullets'
	bid = db.Column(db.Integer, primary_key=True)
	sym_name = db.Column(db.Text, nullable=False)
	content = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
	uid = db.Column(db.Integer, db.ForeignKey('users.uid'))


class Users(db.Model):
	"""users table"""
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.Text,nullable=False, index=True, unique=True)
	true_name = db.Column(db.Text)
	sex = db.Column(db.Text)
	birthday = db.Column(db.DateTime)
	location = db.Column(db.Text)
	email = db.Column(db.Text,nullable=False, unique=True)
	password_md5 = db.Column(db.Text)
	signup_datetime = db.Column(db.DateTime)
	last_signin_datetime = db.Column(db.DateTime)
